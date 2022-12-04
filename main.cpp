#include <iostream>

using namespace std;

int main()
{
    const int N = 100;
    char *str = new char [N];
    int len = 0, k = 0;
    bool f;
    cout << "Vvedite stroki: " << endl;
    for (int i = 1; i <= 3; i++) {
        cin.getline(str, N);
        while (str[len]) {
            len++;
        }
        f = true;
        int j = 0;
        while ((j < len/2) && f) {
            if (str[j] != str[len-1-j]) f = false;
            j++;
        }
        if (f) {
            k++;
        }
    }
    cout << "kol-vo slov palindromov " << k;
    delete str;
    return 0;
}