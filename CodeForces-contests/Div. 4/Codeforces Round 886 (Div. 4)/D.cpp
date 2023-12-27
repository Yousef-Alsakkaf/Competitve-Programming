#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    cin >> T;
    vector<int> arr;
    while(T--)
    {
        int n, k;
        cin >> n >> k;
        arr.resize(n);
        int longestSub = 1;
        int counter = 1;
        for(int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        sort(arr.begin(), arr.end());
        for(int i = 1; i < arr.size(); i++)
        {
            if(arr[i] - arr[i - 1] <= k)
            {
                counter++;
                longestSub = max(counter, longestSub);
            }
            else
            {
                counter = 1;
            }
        }
        cout << n - longestSub << endl;
        arr.clear();
    }
    return 0;
}