#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int sum(vector<int> &nums)
{
    int sum = 0;
    for(int i = 0; i  < nums.size(); i++)
    {
        sum += nums[i];
    }
    return sum;
}
int main()
{
    int num;
    cin >> num;

    vector<int> nums;
    for(int i = 0; i < num; i++)
    {
        int a;
        cin >> a;
        nums.push_back(a);
    }
    sort(nums.begin(), nums.end());
    int s = sum(nums);

    int minimum = 0;
    int minSum = 0;
    for(int i = nums.size() - 1; i >= 0; i--)
    {
        minSum += nums[i];
        if(minSum > s / 2)
        {
            minimum++;
            break;
        }
        else
        {
            minimum++;
        }
    }
    cout << minimum;
    return 0;
}