#include <iostream>
#include <string>

using namespace std;

int main(){
    int n;
    cin >> n;

    int p = 0;
    string r;
    cout << p << flush;
    cin >> r;
    int s = 0;
    int e = n;
    string sc = r;
    string ec = r;
// [0, 1, 2, ..., n] = [r, ., ., ,, ..., r]
// n is odd
// [s, e] = [0, n]
    int former, latter;

    while (1){
        if (r.compare("Vacant") == 0) {break; }
        p = (e - s + 1) / 2;
        if (e - s <= 1) {
            cout << 1 << flush;
            cin >> r;
            if (r.compare("Vacant") == 0) {break; }
        }
        else if (e - s == 2){
            cout << 1 << flush;
            cin >> r;
            if (r.compare("Vacant") == 0) {break; }
            cout << 2 << flush;
            cin >> r;
            if (r.compare("Vacant") == 0) {break; }
        }
        else if (e - s == 3){
            p = 1;
        }
        cout << p << flush;
        cin >> r;
        former = p - s + 1;
        latter = e - p + 1;
        cout << 0 << s << sc << e << ec << endl;

// [0, 1, 2, ..., n] = [r0, ., ., r, ..., r0]
// n is odd
// [s, e] = [0, n], p = (n + 1) / 2
// former = (n + 1) / 2 + 1     5
// latter = (n - 1) / 2 + 1     4
        if (r.compare("Vacant") == 0) {break; }
        if (former % 2 == 0) {
            if (r.compare(sc) == 0){
                // s = s;
                // sc = sc;
                e = p;
                ec = r;
                cout << 0 << s << sc << e << ec << endl;
            }
            else {
                s = p;
                sc = r;
                // e = e;
                // ec = ec;
                cout << 1 << s << sc << e << ec << endl;                
            }
        }
        if (latter % 2 == 0) {
            if (r.compare(ec) == 0){
                s = p;
                sc = r;
                // e = e;
                // ec = ec;
                cout << 1 << s << sc << e << ec << endl;                
            }
            else{
                // s = s;
                // sc = sc;
                e = p;
                ec = r;
                cout << 0 << s << sc << e << ec << endl;                
            }
        }
    }
}


