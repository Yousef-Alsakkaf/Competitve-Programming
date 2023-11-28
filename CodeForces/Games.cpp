#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> homeUniformColors(n);
    unordered_map<int, int> guestUniformColors;

    for (int i = 0; i < n; i++) {
        cin >> homeUniformColors[i];
        int guestUniformColor;
        cin >> guestUniformColor;
        guestUniformColors[guestUniformColor]++;
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        int guestUniformColor = homeUniformColors[i];
        count += guestUniformColors[guestUniformColor];
    }

    cout << count << endl;
    return 0;
}
