#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    return 0;
}

A1 = np.array(map(int, raw_input().split()))
A2 = np.array(map(int, raw_input().split()))
A = np.array([A1, A2], dtype=np.int32)


max_sum = 0
for i in range(0, len(A[0])):
    # print A[0, :i + 1], A[1, i:]
    max_sum = np.max([max_sum, np.sum(A[0, :i + 1]) + np.sum(A[1, i:])])

print max_sum

