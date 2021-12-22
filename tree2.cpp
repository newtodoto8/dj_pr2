#include <bits/stdc++.h>
using namespace std;
class node
{   
public:
     int key;
     node* l_child ;
     node* r_child;
     node* parent;

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
    node* successor(node * root);
    int nochild(node *root);
    node* predecessor(node * root);
    node* _search(int val,node *root);
    int search(int val);
    void remove(int val);


};

void BST:: remove(int val)
{
    node* x=_search(val,root);
    if (nochild(x)==0)
    {
        if (x->key>x->parent->key)
        {
            x->parent->r_child=NULL;
        }
        else
        {
            x->parent->l_child=NULL;
        }
        delete x;
    }

    else if (nochild(x)==1)
    {
        if (x->key>x->parent->key) //determine if x is r_child or l_child
        {
            if (x->l_child==NULL)
            {
                x->parent->r_child=x->r_child;
                x->r_child->parent=x->parent;
            }
            else
            {
                 x->parent->r_child=x->l_child;
                 x->l_child->parent=x->parent;
            }
            delete x;
        }
        else
        {
            if (x->l_child==NULL)
            {
                x->parent->l_child=x->r_child;
                x->r_child->parent=x->parent;
            }
            else
            {
                 x->parent->l_child=x->l_child;
                 x->l_child->parent=x->parent;
            }
            delete x;
        }
       
    }
    else if (nochild(x)==2)
    {
        node* y=_search(successor(x)->key,root);
        int temp=y->key;
        remove(y->key);
        x->key=temp;
        // cout<<successor(x)->key<<endl;
        // y->l_child=x->l_child;
        // y->r_child=x->r_child;
        // y->parent=x->parent;
        
        
    }

    else
    {
        return;
    }
    
}



int BST::search(int val)
{
    node* temp=_search(val,root);
    if (temp==NULL)
    {
        throw std::runtime_error("key not found");
    }
    else
    { return temp->key;}
}

node* BST:: _search(int val, node *root)
{
   if (root==NULL)
   {
    return root;
   } 
   else if (root->key==val)
   {
    return root;
   }
   else if (root->key>val)
   {
    root=root->l_child;
    return _search(val,root);
   }
   else
   {
    root=root->r_child;
    return _search(val,root);
   }
}

int BST::nochild(node *root)
{
    if (root->l_child==NULL && root->r_child==NULL)
    {
        return 0;
    }
    else if (root->l_child==NULL)
    {
        return 1;
    }
    else if (root->r_child==NULL)
    {
        return 1;
    }
    else
    {
        return 2;
    }
}

node* BST::predecessor(node *root)
{
    int val=root->key;
    node *x=root;
    if (x!=NULL)
    {
        x=x->l_child;
    }
    while(x->r_child!=NULL)
    {
        x=x->r_child;
    }
    return x;
}

node* BST::successor(node *root)
{
    int val=root->key;
    node *x=root;
    if (x!=NULL)
    {
        x=x->r_child;
    }

    while (x->l_child!=NULL)
    {
        x=x->l_child;
    }
    // while (!nochild(x))
    // {
    //     if (x->l_child!=NULL)
    //     {
    //         x=x->l_child;
    //     }
    //     else
    //     {
    //         x=x->r_child;
    //     }
    // }
    return x;

}

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
        root->parent=NULL;
    }
    else
    {
        // cout<<"here"<<endl;
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
            y->l_child->parent=y;


        }
        else
        {
            y->r_child=new node;
            y->r_child->key=k;
            y->r_child->l_child=NULL;
            y->r_child->r_child=NULL;
            y->r_child->parent=y;
        }

    }
}
BST:: BST()
{
    root=NULL;
}
void BST::inorder(node *x)
{
    // cout<<"inorder traversal of BST"<<endl;
    if (x==NULL)
    { return;}

    else
    {
    inorder(x->l_child);
    cout<<x->key<<" ";
    inorder(x->r_child);
    }
}
int main()
{
    BST a;
    cout<<endl;
    
    a.insert(51);
    a.insert(23);
    a.insert(34);
    a.insert(24);
    a.insert(114);
    a.insert(4);
    a.insert(134);
    a.insert(104);
    a.insert(109);
    a.insert(113);
    a.insert(54);
    a.insert(41);
    a.insert(35);
    a.inorder(a.root);
    // cout<<endl<<a.nochild(a._search(54,a.root));
    cout<<endl;
    a.remove(34);
    a.inorder(a.root);
    cout<<endl;
    a.remove(35);
    a.inorder(a.root);
    

    // a.remove(51);
    // a.remove(24);
    // a.inorder(a.root);
    // 

}

