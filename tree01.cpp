#include <bits/stdc++.h>
using namespace std;
class node
{   
public:
     int key;
     int height;
     node* l_child ;
     node* r_child;
     node* parent;
   
    
    node(){;}
    node(int k)
    {
        key=k;
        l_child=NULL;
        r_child=NULL;
        parent=NULL;
    }
    int balancefactor()
    {
        if (l_child==NULL && r_child==NULL)
            return 0;
        else if (l_child!=NULL && r_child==NULL)
            return (-1)*l_child->height;
        else if (l_child==NULL && r_child!=NULL)
            return r_child->height;
        else
            return r_child->height-l_child->height;

    }
    

};


class BST
{
public:
    node* root;
    BST()
    {
        root=NULL;
        // cout<<"called const";
    }
    int max_height(node* a, node* b)
    {
        if (a==NULL && b==NULL)
            {return max(0,0);}
        else if (a==NULL && b!=NULL)
            {return max(0,b->height);}
        else if (a!=NULL && b==NULL)
            {return max(0,a->height);}
        else
            {return max(a->height,b->height);}
    }
    void _update_height(node* x)
    {
        if (x==NULL)
        {
            return;
        }

        if (x->parent==NULL)
        {
            return; //root case
        }
        
        // if (x->height+1<=max_height (x->parent->l_child,x->parent->r_child))
        if (x->height+1<=x->parent->height)
        {
            return;
        }
        else
        {
            x=x->parent;
            x->height+=1;
            _update_height(x);
        }
        //extra cautious not necessary x=x->parent is also fine
        // if(x->parent==x->parent->l_child)
        // {
           
        //     if (x->parent->r_child->height>=x->parent->height+1)
        //     {
        //         return;
        //     }
        //     else
        //     {
                

        //     }
            
            
        // }
        // else if(x->parent==x->parent->r_child)
        // {
        //      if (x->parent->l_child->height>=x->parent->height+1)
        //     {
        //         return;
        //     }
        //     else
        //     {
        //         x->height+=1;
        //         x=x->parent;
        //         _update_height(x);
        //     }
        // }

        // else
        //     {return;}
    }

    void anticlock_turn(node* y)
    {
      
        if (y->parent==root)
        {
              
            node* temp =new node;
            temp=root;
            root=y;
            root->l_child=temp;
            // root->l_child->parent=root;
            root->l_child->r_child=NULL;
            // root->parent=NULL;
            cout<<"fn called ujp"<<endl;
        }
        else
        {
            node* temp=y->parent;
            y->parent=temp->parent;
            y->l_child=temp;
            temp->r_child=NULL;
            temp->parent=y;

        }
    }
    void elbow_turn_ac(node* y)
    {
        ;
    }
    void elbow_turn_c(node* y)
    {
        ;
    }
    void clock_turn(node*y)
    {
        ;
    }
    void manage_height(node *x)
    {
        cout<<"manage_height called"<<endl;
        node* y=x;
        node* z=x->parent;
        while(z!=NULL)
        {
            if (z->balancefactor()==2 and y->balancefactor()==1)
            {
                cout<<"anticlock_turn "<<z->key<<" "<<y->key<<" root or not "<<(y->parent==root)<<endl;
                anticlock_turn(y);
            }
            else if  (z->balancefactor()==2 and y->balancefactor()==-1)
            {
                elbow_turn_ac(y);
            }
            else if  (z->balancefactor()==-2 and y->balancefactor()==1)
            {
                clock_turn(y);
            }
            else if  (z->balancefactor()==-2 and y->balancefactor()==1)
            {
                elbow_turn_c(y);
            }
            else
            {
                ;
            }
            z=z->parent;
            y=y->parent;
        }
    }
    int high(node* a)
    {
        if(a==NULL)
        {
            return 0;
        }
        else return a->height;
    }

    node* insert(int k)
    {
        node *y=new node;
        if (root==NULL)
            // cannot make assignments to null pointer 
        {
            root=y;
            root->key=k;
            root->l_child=NULL;
            root->r_child=NULL;
            root->parent=NULL;
            root->height=1;
            // cout<< "here"<<endl;
            _update_height(root);
            manage_height(root);
            return root;

        }
        else
        {
            // cout<< "there"<<endl;
            node* x= new node;
            x=root;
            while(x!=NULL)
            {
                    y=x;
                
                    if (k<x->key)
                    {
                        x=x->l_child;
                    }
                    else
                    {
                        x=x->r_child;
                    }
            }

        // before assigning anything using arrow operator ensure that the pointer is not null(null has no type)
        node* z=new node;
        x=z;
        x->parent=y;
        x->key=k;
        x->l_child=NULL;
        x->r_child=NULL;
        x->height=1;
        

        if (k<y->key)
        {
            y->l_child=x;
        } 
        else y->r_child=x;

        _update_height(x);
        manage_height(x);
        return x;
        }

        
    }

    void inorder(node* a)
    {   
        node* x=a;
        if(x!=NULL)
        {
            inorder(x->l_child);
            cout<<" key: "<<x->key<<" height "<<x->height<<" "<<" balancefactor "<<x->balancefactor()<<" ";
            inorder(x->r_child);
        }
        else return;

    }
};



// BST::BST(int k)
// {
//     root->key=k;
//     root->l_child=NULL;
//     root->r_child=NULL;
//     root->parent=NULL;
// }

int main()
{
    BST a;
    int arr[3];
    cout<<endl;
    srand(time(0));
    for(int i=0; i<3;i++)
    {   
        // int temp=rand()%100;
        // a.insert(temp);
        // arr[i]=temp;

        cin>>arr[i];
        a.insert(arr[i]);
    }
    
    for(int i=0; i<3;i++)
    {   
        cout<<arr[i]<<" ";
    }
    cout<<a.root->key<<" "<<a.root->l_child->key <<" xz"<<a.root->r_child->key<<endl;
    a.inorder(a.root);
    
   
    return 0;



}