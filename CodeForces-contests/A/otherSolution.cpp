#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main() {
    int T; // number of test cases
    cin >> T;

    while (T--) {
        int size;
        cin >> size;

        unordered_set<int> x_set, y_set;

        for (int i = 0; i < size; i++) {
            int a, b;
            cin >> a >> b;
            x_set.insert(a);
            y_set.insert(b);
        }

        int counter = 0;

        if (!x_set.empty() && *max_element(x_set.begin(), x_set.end()) > 0) {
            counter++;
        }
        if (!x_set.empty() && *min_element(x_set.begin(), x_set.end()) < 0) {
            counter++;
        }
        if (!y_set.empty() && *max_element(y_set.begin(), y_set.end()) > 0) {
            counter++;
        }
        if (!y_set.empty() && *min_element(y_set.begin(), y_set.end()) < 0) {
            counter++;
        }

        if (counter <= 3) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
