#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) return false;

        vector<int> arr(26, 0);
        for(char c : s)
        {
            arr[c-'a']++;
        }
        for(char c : t)
        {
            arr[c-'a']--;
        }
        for(int num : arr)
        {
            if(num != 0)
            {
                return false;
            }
        }
        return true;
    }
};