#include<iostream>
#include<string>
using namespace std;
main()
{
	string a, b, c;
	int n;
	cin>>a>>b>>c;
	n=0;
	while (n!=-1)
	{
		cout<<c;
		n=a.find(b);
		cout<<a.substr(0,n);
		a.erase(0,n+1);
	}
}
