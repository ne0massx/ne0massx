#include<iostream>
#include<string>
using namespace std;
main()
{
	string a, b, c;
	int n;
    getline(cin,a);
	n=0;
	while (n!=-1)
	{
		n=a.find('/');
		cout<<a.substr(0,n)<<endl;
		a.erase(0,n+1);
	}
}
