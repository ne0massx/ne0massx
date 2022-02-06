#include<iostream>
using namespace std;
main()
{
  int N=0, A[101];
  cin >> N;
  A[0]=1;
  for(int i=1; i<N; i++)
  A[i]=A[i-1]*2;
  for(int i=0; i<N; i++)
  cout<<A[i]<<" ";
}
