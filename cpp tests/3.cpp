#include<iostream>
#include<string>
using namespace std;
main()
{
 int n, k;
 string s;
 cin>>n;
  cout<<n<<endl;
 for (int i=0; i<n; i++) 
 {
  cin>>s>>k;
  cout<<s<<" "<<++k<<endl;
 }
}

