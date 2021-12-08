#include <bits/stdc++.h>
using namespace std;


class color
{
private:
	int r;
	int g;
	int b;
	int rgb[3];
public:
	color(int a,int b,int c)
	{
		r=a;
		g=b;
		b=c;
	}

	int* returnrgb()
	{
		return this->rgb;
	}
};

class cube
{
public:
	cube(int len,color c)
	{
		len=len;
		c=c;

	}
private:
	int len;
	color c;
};

class stack
{
public:
	std::vector<cube> cubes_;

	std::ostream& operator<<(std::ostream& os,const stack& st)
	{
		for (auto& iter_var : cubes_)
		{
			cout<<iter_var<<endl;
		}
	}
}

class Hanoi
{
public:
	std::vector<stack> stacks_[3];

	void solve();


}