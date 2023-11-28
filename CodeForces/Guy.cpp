#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
    int length;
    cin >> length;
    unordered_set<int> set;

    int p;
    cin >> p;
    for(int i = 0; i < p; i++){
        int a;
        cin >> a;
        set.insert(a);
    }
    int q;
    cin >> q;
    for(int i = 0; i < q; i++)
    {
        int a;
        cin >> a;
        set.insert(a);
    }
    if(set.size() == length)
    {
        cout << "I become the guy.";
    }
    else
    {
        cout << "Oh, my keyboard!";
    }
    return 0;
}