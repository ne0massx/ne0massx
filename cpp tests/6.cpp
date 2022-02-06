#include<iostream>
using namespace std;
long long n,k;
long long cmp(long long z, long long y, long long d) {
    if (z > y) swap (z, y);
    if ( d - z < y - d ) return z;
    if ( d - z > y - d ) return y;
    return z;
}
int main()
{
    long long a[100001], b[100001];
    cin >> n >> k;
    for (long long i = 0; i < n; i++) {
        cin>>a[i];
    }
    for (long long i = 0; i < k; i++) {
        cin >> b[i];
    }
    for (long long i = 0; i < n; i++) {
        long long x=b[i];
        long long l = 0, r = n - 1;
        while (r - l > 1) {
            long long m = (l + r) / 2;
            if (a[m] > x) r = m;
            else l = m;
        }
        long long ans = cmp(a[l], a[r], x);
        cout << ans << '\n';
    }
    return 0;
    
}
