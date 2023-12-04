#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map; // key = num, value = index
        
        for(int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];
            auto it = map.find(diff);
            if(it != map.end())
            {
                return {map[diff], i};
            }
            map[nums[i]] = i;
        }
        return {};
    }
};