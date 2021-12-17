#include <bits/stdc++.h>
using namespace std;
class node
{   
public:
     int key;
     node* l_child ;
     node* r_child;
     node()
     {
        ;
     }
 
    node(int k)
    {
        key=k;
        l_child=NULL;
        r_child=NULL;

    }
};

class BST
{
public:
    node *root;
    BST();
    void insert(int k);
    void inorder(node *root);
};




void BST::insert(int k)
{
    if (root==NULL)
    {
        node *r=new node;
        root=r;
        cout<<"root was empty "<<endl;
        root->key=k;
        root->l_child=NULL;
        root->r_child=NULL;
        
    }
    else
    {
        cout<<"here"<<endl;
        node *r=new node;
        r=root;
        node *y =r;
        while(r!=NULL)
        {
            // cout<<"loop yaya"<<endl;
            y=r;
            if (r->key>k)
            {
                r=r->l_child;
            }
            else r=r->r_child;
        }
        if (y->key>k)
        {
            y->l_child=new node;
            y->l_child->key=k;
            y->l_child->l_child=NULL;
            y->l_child->r_child=NULL;


        }
        else
        {
            y->r_child=new node;
            y->r_child->key=k;
            y->r_child->l_child=NULL;
            y->r_child->r_child=NULL;
        }

    }
}
BST:: BST()
{
    root=NULL;
}
void BST::inorder(node *x)
{
    if (x==NULL)
    { return;}

    else
    {
    inorder(x->l_child);
    cout<<x->key<<endl;
    inorder(x->r_child);
    }
}
int main()
{
    BST a;
    cout<<"dbvcbasda"<<endl;
    a.insert(51);
    a.insert(23);
    a.insert(34);
    a.insert(24);
    a.insert(114);
    a.insert(4);
    a.insert(134);
    a.insert(41);
    a.inorder(a.root);

}

