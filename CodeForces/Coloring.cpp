#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void solve(vector<int> nums)
{
    int left = 0, right = nums.size() - 1, counter = 0;
    while(left < right)
    {
        counter += nums[right] - nums[left];
        left++;
        right--;
    }
    cout << counter << endl;
}
int main()
{
    int T;
    cin >> T;
    vector<int> nums;
    while(T--)
    {
        int size;
        cin >> size;
        nums.resize(size);
        for(int i = 0; i < nums.size(); i++)
        {
            int a;
            cin >> a;
            nums[i] = a;
        }
        sort(nums.begin(), nums.end());
        solve(nums);
        nums.clear();
    }
    return 0;
}