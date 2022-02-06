#include<iostream>
using namespace std;
main()
{
int n, count;
cin >> n;
count = 0;
while (n != 0) 
  {
  count ++;
  n = n / 10;
  }
cout << "Number " <<n<< " contains " << count << " digits";
}
