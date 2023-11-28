#include <iostream>
#include <unordered_set>

using namespace std;
int main(){
    unordered_set<int> set;
    for(int i = 0; i < 4; i++){
        int a;
        cin >> a;
        set.insert(a);
    }
    int ans = 4 - set.size();

    cout << ans;
    return 0;
}