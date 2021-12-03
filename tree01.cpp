#include <bits/stdc++.h>
using namespace std;
struct node
{
     int key;
     node* l_child ;
     node* r_child;
     node* parent;
};


class BST
{
public:
    node* root=NULL;

    void insert(int k)
    {
        
        node* y=NULL;
        if (root==NULL)
        {
            root->key=k;
            root->l_child=NULL;
            root->r_child=NULL;
            root->parent=NULL;
            cout<< "here";

        }
        else
        {
            cout<< "there";
            node* x=root;
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
        x->parent=y;
        if (k<y->key)
        {
            y->l_child=x;
        } 
        else y->r_child=x;
        }
    }

    void inorder(node* a)
    {   
        node* x=a;
        if(x!=NULL)
        {
            inorder(x->l_child);
            cout<<x->key;
            inorder(x->r_child);
        }
        else return;

    }
};

int main()
{
    // BST a;
    // a.insert(10);
    // a.insert(12);
    // a.insert(23);
    // a.inorder(a.root);
    cout<<"dsad";



}