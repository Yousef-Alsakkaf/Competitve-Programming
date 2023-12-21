#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size() - 1;
        int res = nums[0];

        while(left <= right)
        {
            if(nums[left] < nums[right])
            {
                res = min(res, nums[left]);
                break;
            }

            int mid = left + (right - left) / 2;
            res = min(res, nums[mid]);
            if(nums[mid] >= nums[left]) left = mid + 1;
            else right = mid - 1;
        }
        return res;
    }
};