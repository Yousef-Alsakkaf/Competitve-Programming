#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<char>> array(n, vector<char>(n));
    char d, o;
    bool t = true;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> array[i][j];
            d = array[0][0];
            o = array[0][1];

            if (i == j) {
                if (array[i][j] != d) {
                    t = false;
                }
            } else if (i + j == n - 1) {
                if (array[i][j] != d) {
                    t = false;
                }
            } else {
                if (array[i][j] != o) {
                    t = false;
                }
            }
        }
    }
    if(o == d) t = false;

    if (t) {
        cout << "YES";
    } else {
        cout << "NO";
    }

    return 0;
}
