#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
    int length;
    cin >> length;

    string word;
    cin >> word;

    unordered_set<char> set;
    for(int i = 0; i < length; i++)
    {
        set.insert(tolower(word.at(i)));
    }
    if(set.size() == 26)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}