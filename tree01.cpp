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
            return this->height-l_child->height;
        else if (l_child==NULL && r_child!=NULL)
            return r_child->height-this->height;
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
    void _update_height(node* x)
    {
        
        //extra cautious not necessary x=x->parent is also fine
        if(x->parent==x->parent->l_child)
        {
           
            if (x->parent->r_child->height>=x->parent->height+1)
            {
                return;
            }
            else
            {
                x->height+=1;
                x=x->parent;
                _update_height(x);
            }
            
            
        }
        else if(x->parent==x->parent->r_child)
        {
             if (x->parent->l_child->height>=x->parent->height+1)
            {
                return;
            }
            else
            {
                x->height+=1;
                x=x->parent;
                _update_height(x);
            }
        }

        else
            {return;}
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
            root->height=0;
            // cout<< "here"<<endl;
            _update_height(root);
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
        x->height=0;
        

        if (k<y->key)
        {
            y->l_child=x;
        } 
        else y->r_child=x;

        _update_height(x);
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
    int arr[7];
    cout<<endl;
    srand(time(0));
    for(int i=0; i<7;i++)
    {   
        // int temp=rand()%100;

        cin>>arr[i];
        a.insert(arr[i]);
    }
    
    for(int i=0; i<7;i++)
    {   
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    a.inorder(a.root);
    
   
    return 0;



}