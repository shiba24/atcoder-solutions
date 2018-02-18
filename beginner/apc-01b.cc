#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    int a[n];
    int b[n];
    int asum = 0;
    int bsum = 0;

    int p = 0;

    for (int i = 0; i < n; i++){
        cin >> p;
        a[i] = p;
        asum += p;
    }
    p = 0;
    for (int i = 0; i < n; i++){
        cin >> p;
        b[i] = p;
        bsum += p;
    }
    string s;
    if (asum < bsum) {
        int onediff = 0;
        int twodiff = 0;
        for (int i = 0; i < n; i++){
            if (a[i] > b[i]){onediff += a[i] - b[i]; }
            else {twodiff += b[i] - a[i];}
        }
        if (onediff > n){s = "No"; }
        if (twodiff > n * 2){s = "No"; }
        else {s = "Yes";}
    }
    else if (asum == bsum){
        int i = 0;
        s = "Yes";
        for (int i = 0; i < n; i++){
            if (a[i] != b[i]){
                s = "No";
                break;
            }
        }
    }
    else {s = "No";}
    cout << s << endl;
    return 0;
}
