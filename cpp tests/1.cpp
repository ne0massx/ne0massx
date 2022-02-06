#include<iostream>
#include<string>
using namespace std;
main()
{
 string s;
 cin>>s;
 for (int i=0; i<s.size(); i++)	
  if (s[i]=='a') s[i]='b';
  else
      if (s[i]=='A') s[i]='B';
      else 
	      if (s[i]=='b') s[i]='a';
	      else
	           if (s[i]=='B') s[i]='A';
cout<<s;
}
