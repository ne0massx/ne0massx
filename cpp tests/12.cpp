#include<iostream>
#include<string>
using namespace std;
main()
{
	string a, b="", c;
	int n=0;
	
	while (cin>>a){
		b=b+' '+a;
		
	}
	b.erase(0,1);
		cout<<b;
}
