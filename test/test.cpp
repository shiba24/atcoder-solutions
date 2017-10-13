#include <iostream>
using namespace std;


void count(int i){
    if (i > 0){
        for (int k = i; k > 0; k--){
            cout << k << endl;
        }
        cout << "fin!" << endl;
    }
    else {cout << "input negative value: " << i << endl;}
}


int main(){
    int i;
    cout << "Please input number: ";
    cin >> i;
    count(i);
    return 0;
}

