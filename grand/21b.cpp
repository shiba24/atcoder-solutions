#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iterator>

using namespace std;

int M = 50;
int n;
int x, y;


int check(int i, int j, vector<vector<float> > hole){
    int ith = 0;
    long dist = 2000000;
    for (int k = 0; k < hole.size(); k++ ){
        int d = abs(i - hole[k][0]) + abs(j - hole[k][1]);
        if (d < dist){
            ith = k;
            dist = d;
        }
    }
    return ith;
}

vector<float> standardize(vector<int> cnt){
    float sum = 0.0;
    vector<float> st;
    st.resize(cnt.size());

    for (int k = 0; k < cnt.size(); k++ ){
        sum += cnt[k];
    }
    for (int k = 0; k < cnt.size(); k++ ){
        st[k] = cnt[k] / sum;
    }
    return st;
}


vector<int> ith_cnt(vector<int> I){
    if (I.size() == 1){
        return I;
    }
    else if (I[0] == I[I.size()]){
        for (int i = 0; i < I.size(); i++){
            I[i] = I[0];
        return I;
        }
    }
    else {
        vector<int> v1;
        vector<int> v2;
        vector<int> nv1;
        vector<int> nv2;
        v1 = vector<int> (I.begin(), I.begin() + I.size() / 2);
        v2 = vector<int> (I.begin() + I.size() / 2, I.end());

        // copy(I.front(), I[I.size() / 2], v1);
        // copy(I[I.size() / 2], I.back(), v2);
        nv1 = ith_cnt(v1);
        nv2 = ith_cnt(v2);
        nv1.insert(nv1.end(), nv2.begin(), nv2.end());
        // copy(nv2.begin(), nv2.end(), back_inserter(nv1));
        return nv1;
    }
}


vector<int> cnt_row(int i, vector<int> ith, vector<int> cnt,  vector<vector<float> > hole){

    vector<int> new_cnt;
    // new_cnt = cnt;
    // copy(cnt.front(), cnt.back(), new_cnt);

    ith.front() = check(i, ith.front(), hole);
    ith.back() = check(i, ith.back(), hole);

    vector<int> ith_c = ith_cnt(ith);


    for (int i = 0; i < n; i ++){
        new_cnt[i] += count(ith_c.begin(), ith_c.end(), i);
    }
    return new_cnt;
}



int main(){
    cin >> n;
    vector<vector<float> > hole;
    hole.resize(n);
    for(int i = 0; i < n; i++){
        hole[i].resize(2);
        cin >> x >> y;
        hole[i][0] = x;
        hole[i][0] = y;
    }

    vector<int> cnt;
    cnt.resize(n);

    for (int i = -1 * M; i < M; i++){
        vector<int> ith;
        ith.reserve(2 * M);
        for (int j = 0; j < 2 * M; j++){
            // ith.emplace_back(j);
            ith[j] = j - M;
        }

        cnt = cnt_row(i, ith, cnt, hole);
    }

    vector<float> st;
    st = standardize(cnt);

    for (int i = 0; i < n; i++){
        cout << st[i] << endl;
    }
    return 0;
}
