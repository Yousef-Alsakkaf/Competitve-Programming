#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

int main()
{
    string input;
    getline(cin, input);
    unordered_set<char> set;

    for(char c : input)
    {
        if(isalpha(c))
        {
            set.insert(c);
        }
    }
    cout << set.size();
    return 0;
}