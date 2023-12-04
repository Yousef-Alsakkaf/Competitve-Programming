#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(string word : strs)
        {
            string newWord = orderWord(word);
            auto it = map.find(newWord);
            map[newWord].push_back(word);
        }
        vector<vector<string>> answer;
        for(auto it = map.begin(); it != map.end(); it++)
        {
            answer.push_back(it -> second);
        }
        return answer;
    }
    string orderWord(string word)
    {
        sort(word.begin(), word.end());
        return word;
    }
};