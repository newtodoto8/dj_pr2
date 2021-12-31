#include <iostream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>


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
    node* predecessor(node* x)
    {
        if (x==NULL) return NULL;

        x=x->l_child;
        node* y=new node;
        y=x;
        while(x!=NULL)
        {
            y=x;
            x=x->r_child;
        }
        return y;
    }

    node* anticlock_turn(node* y)
    {

        if (y->parent==root)
        {

            node* temp =new node;
            temp=root;
            root=y;
            root->parent=NULL;
            root->l_child=temp;
            // root->l_child->parent=root;
            root->l_child->r_child=NULL;
            temp->parent=root;
            temp->r_child=NULL;
            temp->height-=2;
            cout<<"fn called to change structure"<<endl;
            return root;
        }
        else
        {
            cout<<" y->parent "<<y->parent->key<<endl;
            cout<<" y->r_child "<<y->r_child->key<<" y "<<y->key<<" root: " <<root->key <<" root_lchild: " <<root->l_child->key<<" rootri8 "<<root->r_child->key<<endl;

            node* temp=new node;
            temp=y->parent;
            y->parent=temp->parent;


            temp->parent->r_child=y;
            temp->parent=y;
            y->l_child=temp;
            temp->r_child=NULL;

            temp->height-=2;
            return y;
            cout<<"2nd structure change cond called"<<endl;
            cout<<" y->parent "<<y->parent->key<<" y->l_child "<<y->l_child->key<<" temp: " <<temp->key <<endl;
            cout<<" y->r_child "<<y->r_child->key<<" y "<<y->key<<" root: " <<root->key <<" root_lchild: " <<root->l_child->key<<" rootri8 "<<root->r_child->key<<endl;

        }
    }
    node* elbow_turn_ac(node* y)

    {
        cout<<"y->key: "<<y->key<<endl;
        node* temp=new node;
        temp=y;
        temp->parent->r_child=y->l_child;
        y->l_child->parent=temp->parent;
        y->l_child->r_child=temp;
        y->l_child->l_child=NULL;
        temp->parent=y->l_child;
        temp->l_child=NULL;
        node* k=new node;
        k=anticlock_turn(temp->parent);
        return(k);

    }
    node* elbow_turn_c(node* y)
    {
          cout<<"y->key: "<<y->key<<endl;
        node* temp=new node;
        temp=y;
        temp->parent->l_child=y->r_child;
        y->r_child->parent=temp->parent;
        y->r_child->l_child=temp;
        y->r_child->r_child=NULL;
        temp->parent=y->r_child;
        temp->r_child=NULL;
        node* k=new node;
        k=anticlock_turn(temp->parent);
        return(k);
    }
    node* clock_turn(node* y)
    {
        if (y->parent==root)
        {

            node* temp =new node;
            temp=root;
            root=y;
            root->parent=NULL;
            root->r_child=temp;
            // root->l_child->parent=root;
            root->r_child->l_child=NULL;
            temp->parent=root;
            temp->l_child=NULL;
            temp->height-=2;
            cout<<"fn called to change structure"<<endl;
            return root;
        }
        else
        {
            cout<<" y->parent "<<y->parent->key<<endl;
            cout<<" y->l_child "<<y->l_child->key<<" y "<<y->key<<" root: " <<root->key <<" root_lchild: " <<root->l_child->key<<" rootri8 "<<root->r_child->key<<endl;

            node* temp=new node;
            temp=y->parent;
            y->parent=temp->parent;


            temp->parent->l_child=y;
            temp->parent=y;
            y->r_child=temp;
            temp->l_child=NULL;

            temp->height-=2;
            return y;
            cout<<"2nd structure change cond called"<<endl;
            //cout<<" y->parent "<<y->parent->key<<" y->l_child "<<y->l_child->key<<" temp: " <<temp->key <<endl;
            //cout<<" y->r_child "<<y->r_child->key<<" y "<<y->key<<" root: " <<root->key <<" root_lchild: " <<root->l_child->key<<" rootri8 "<<root->r_child->key<<endl;

        }
    }
    void _update_height2(node* x)
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
        if (x->height+1!=x->parent->height)
        {
            x=x->parent;
            x->parent->height-=1;
            _update_height2(x);
            return;
        }
        else
        {
            x=x->parent;
            _update_height2(x);
            
        }
    }
    node* manage_height(node *x)
    {
        cout<<"manage_height called"<<endl;
        if (x->parent!=NULL)
        {
            cout<<"x->height "<<x->height<<endl;
            cout<<"x->key : "<<x->key<<endl;
            cout<<"x->parent->key : "<<x->parent->key<<endl;
        }
        node* y=x;
        node* z=x->parent;

        if (y)
        {
        cout<<"y->balancefactor "<<y->balancefactor()<<endl;
        }
        if (z)
        {
            cout<<"z->balancefactor "<<z->balancefactor()<<endl;
        }
        while(z!=NULL)
        {
            node* k=new node;
            if (z->balancefactor()==2 and y->balancefactor()==1)
            {
                cout<<"anticlock_turn "<<z->key<<" "<<y->key<<" root or not "<<(y->parent==root)<<endl;
                k=anticlock_turn(y);

                return k;
            }
            else if  (z->balancefactor()==2 and y->balancefactor()==-1)
            {
                cout<<"elbow_turn_ac"<<endl;
                k=elbow_turn_ac(y);
                 return k;
            }
            else if  (z->balancefactor()==-2 and y->balancefactor()==-1)
            {
                cout<<"clock_turn"<<endl;
                k=clock_turn(y);
                 return k;
            }
            else if  (z->balancefactor()==-2 and y->balancefactor()==1)
            {
                k=elbow_turn_c(y);
                 return k;
            }
            else
            {
                if(y && z){

                cout<<"z: "<<z->key<<endl;

                cout<<"y: "<<y->key<<endl;
            }
            z=z->parent;
             y=y->parent;

            }

        }
        return NULL;
    }


    node* insert(int k)
    {
        node *y=new node;
        if (root==NULL)
            // cannot make assignments to null pointer
        {
            cout<<"root assigned"<<endl;
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
        node* ret=new node;
        ret=manage_height(x);
        _update_height2(ret);
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

     void preorder(node* a)
    {
        node* x=a;
        if(x!=NULL)
        {
            cout<<" key: "<<x->key<<" height "<<x->height<<" "<<" balancefactor "<<x->balancefactor()<<" ";
            preorder(x->l_child);

            preorder(x->r_child);
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
    int arr[15];
    cout<<endl;
    srand(time(0));
    for(int i=0; i<15;i++)
    {
        // int temp=rand()%100;
        // a.insert(temp);
        // arr[i]=temp;

        // cin>>arr[i];
        // a.insert(arr[i]);
    }

    for(int i=0; i<5;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    a.preorder(a.root);
    cout<<"\nroot->r_child "<<a.root->r_child->key<<endl;
    cout<<"predeccessor "<<a.predecessor(a.root)->key<<endl;
    a.inorder(a.root);


    return 0;



}