#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isValidK(long long k, const vector<long long>& arr) {
    vector<long long> result;
    for (long long a : arr) {
        result.push_back(a % k);
    }
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result.size() == 2;
}

long long findK(const vector<long long>& arr) {
    long long low = 1, high = 1e18, result = 1;

    while (low <= high) {
        long long mid = (low + high) / 2;
        if (isValidK(mid, arr)) {
            result = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return result;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<long long> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        long long k = findK(arr);
        cout << k << endl;
    }

    return 0;
}
