#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isSorted(const vector<int>& nums);

int main()
{
    int n;
    cin >> n;
    bool isRated = true;
    vector<int> nums;  // Remove the size parameter from here

    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        if (a != b)
        {
            isRated = false;
        }
        else
        {
            nums.push_back(a);
        }
    }

    if (!isRated)
    {
        cout << "rated";
    }
    else
    {
        bool sorted = isSorted(nums);
        if (sorted)
        {
            cout << "maybe";
        }
        else
        {
            cout << "unrated";
        }
    }

    return 0;
}

bool isSorted(const vector<int>& nums)
{
    
    bool decreasing = is_sorted(nums.rbegin(), nums.rend());

    return decreasing;
}
