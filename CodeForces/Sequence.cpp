#include <iostream>
#include <vector>
using namespace std;

void solve(vector<int> nums)
{
    int left = 0, right = nums.size() - 1;
    while (left <= right) 
    {
        if(left < right)
        {
            cout << nums[left] << " " << nums[right] << " ";
        }
        else cout << nums[left] << " ";
        left++;
        right--;
    }
    cout << endl;
}

int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int size;
        cin >> size;
        vector<int> nums(size);
        for(int i = 0; i < nums.size(); i++)
        {
            int a;
            cin >> a;
            nums[i] = a;
        }
        solve(nums);
    }
    return 0;
}
