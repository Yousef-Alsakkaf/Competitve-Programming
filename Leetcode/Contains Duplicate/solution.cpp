#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for(int num : nums)
        {
            auto it = set.find(num);
            if(it != set.end())
            {
                return true;
            }
            set.insert(num);
        }
        return false;
    }
};