#include<bits/stdc++.h>
using namespace std;
int main() {
    int n = 200;
    unsigned int f[200] = {0};

    unsigned int a = 0;
    unsigned int b = 1;
    unsigned int c = 0;
    for(int i = 0; i < n; i++) {
        c = a + b;
        f[i] = c;
        cout << f[i] << endl;
        a = b;
        b = c;
    }
    
}