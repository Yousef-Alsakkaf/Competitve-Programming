#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        
        while(left <= right)
        {
            int middle = (left + right) / 2;
            if(nums[middle] == target)
            {
                return middle;
            }
            else if(nums[middle] < target)
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        return - 1;
    }
};