#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector<int> nums;
    int num;
    cin >> num;

    for(int i = 0; i < num; i++)
    {
        int a;
        cin >> a;
        nums.push_back(a);
    }
    sort(nums.begin(), nums.end());

    int counter = 0;
    for(int i = 1; i < nums.size() - 1; i++)
    {
        if(nums[i] > nums[0] && nums[i] < nums[nums.size() - 1])
        {
            counter++;
        }
    }
    cout << counter;

    return 0;
}