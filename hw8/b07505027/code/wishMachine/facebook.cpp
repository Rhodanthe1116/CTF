#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n = 200;
    unsigned int f[200] = {0};

    unsigned int sum = 0xFAC0B00C;
    for (int i = 0; i < n; i++)
    {
        if (i & 1)
        {
            sum -= 0x78;
        }
        else
        {
            sum -= 0x7788;
        }
        f[i] = sum;
        cout << f[i] << endl;
    }
}