#include <bits/stdc++.h>
using namespace std;

// class samp
// {
// public:
// 	int value;
// 	samp(int a)
// 	{
// 		cout<<"constructor called" <<endl;
// 		value=a;
// 	}

// 	samp(const samp& a)
// 	{
// 		cout<<"copy constructor called" <<endl;
// 	}
// 	samp()
// 	{
// 		cout<< "custom default constructor called" <<endl;
// 	}

// 	samp& operator=(const samp& a)
// 	{
// 		this->value=a.value;
// 		cout<<"assignment operator called"<<endl;
// 		return *this;
// 	}
	
	
// };
// void fun(samp &a)
// {
// 	cout<<"pass by ref: "<<a.value<<endl;
// }
// int main()
// {
// 	/* code */
// 	samp a(17);
// 	samp b;
// 	 b=a;
// 	fun(a);
// 	fun(b);


// 	// a=4;

// 	// cout<<a<<endl;
// 	// cout<<&a<<endl;
// 	// // cout<<*a<<endl;


// 	// cout<<y<<endl;
// 	// cout<<&y<<endl;
// 	// cout<<*y<<endl;

// 	return 0;
// }
// template <typename T>
// class ListNode
// {
// public:
// 	T & data;
// 	ListNode(T & data):data(data){}
// };
// void fun(int & data)
// {
// 	cout<<"data is :  "<<data<<endl;
// }
int arpit=1;
template <typename T>
class samp
{
private:
	T  data;

public:

	samp()
	{
		cout<<"default initializer defined as we used T";
	}
	samp(T dat):data(dat)
	{
	}
	T getdata(){
		return data;
	}
	void setdata(int a)
	{
		data=a;
	}
	void print()
	{
		cout<<"dummy class call";
	}

	
	
};

int main()
{
	
	// int a=30;
	// int sum=0;
	// while(std::cin>>a)
	// {
	// 	sum+=a;
	// }
	// cout<<sum;	
	// // int & data;

	// int arpit=12;
	// cout<<arpit<<endl; //outputs 12
	// cout<<::arpit; //outputs 1 global var explicitly requested
	// // ListNode<int> a(10);

	// int &b=a; //int &b=10; fails
	// const int &d=13; //ok
	// int c=10;
	// c=b;
	// b=10;
	// cout<<b<<" "<<c<<" "<<d;
	// samp a(10);
	// a.print();
	// cout<<a.getdata();
	// samp<int> a;
	// samp<int> *b;
	// b=NULL;
	// int aa=12;
	// b->setdata(aa);

	// cout<<b->getdata();
	// cout<<"dsdad";
	samp<int> a;
	a.setdata(12);
	cout<<a.getdata();
	return 0;
}