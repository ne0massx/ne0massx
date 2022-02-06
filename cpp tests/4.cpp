#include<iostream>
#include<string>
using namespace std;
main()
{
	int X, L, R, c,N;
	cin>>N;
	int A[N];
	for (int i=0; i<N; i++)
	cin>>A[i];
	cin>>X;
	L = 0; R=N;
	while ( L<R-1 )
	{
		c = (L+R) / 2;
		if ( X<A[c] )
			R = c;
		else L = c;
	}
	if ( A[L] == X )
		cout<<A[L];
	else cout<<-1;
}
