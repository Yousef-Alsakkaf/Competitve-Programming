#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    vector<string> ans(T);
    for(int i = 0; i < T; i++)
    {
        string a;
        cin >> a;
        int counter = 0;
        if(a.length() > 10)
        {
            counter = a.length() - 2;
            ans.push_back(a[0] + to_string(counter) + a[a.length() - 1]);
        }
        else
        {
            ans.push_back(a);   
        }
    }
    for(int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << endl;
    }
    return 0;
}