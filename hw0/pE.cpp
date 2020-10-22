#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{

    ios::sync_with_stdio(0);
    cin.tie(0);

    byte[] array = new byte[] {
        250,
        241,
        107,
        182,
        244,
        110,
        21,
        129,
        17,
        240,
        155,
        200,
        111,
        111,
        225,
        110,
        180,
        224,
        156,
        194,
        29,
        106,
        141,
        216,
        99,
        58,
        59,
        191,
        45,
        227,
        184,
        221,
        63,
        139,
        223,
        232,
        129,
        201,
        121,
        62,
        164,
        113,
        247,
        230,
        67,
        108,
        182,
        231
    };
    byte[] array2 = list.ToArray();
    int array3[256] = {0};
    int array4[256] = {0};
    byte[] array5 = new byte[array.Length];
    int j;
    for (j = 0; j < 256; j++) {
        array3[j] = (int)array2[j % array2.Length];
        array4[j] = j;
    }
    int num;
    for (j = (num = 0); j < 256; j++) {
        num = (num + array4[j] + array3[j]) % 256;
        int num2 = array4[j];
        array4[j] = array4[num];
        array4[num] = num2;
    }
    int num3;
    num = (num3 = (j = 0));
    while (j < array.Length) {
        num3++;
        num3 %= 256;
        num += array4[num3];
        num %= 256;
        int num2 = array4[num3];
        array4[num3] = array4[num];
        array4[num] = num2;
        int num4 = array4[(array4[num3] + array4[num]) % 256];
        array5[j] = (byte)((int)array[j] ^ num4);
        j++;
    }
}