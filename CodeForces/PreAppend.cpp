#include <iostream>
#include <vector>
using namespace std;
void solve(vector<int> binNums)
{
    int left = 0, right = binNums.size() - 1, counter = 0;
    while(left < right)
    {
        if(binNums[left] != binNums[right])
        {
            counter+= 2;
            left++;
            right--;
        }
        else break;
    }
    cout << binNums.size() -  counter << endl;
}
int main()
{
    int T;
    cin >> T;
    vector<int> binNums;
    while(T--)
    {
        int length;
        cin >> length;
        binNums.resize(length);
        for(int i = 0; i < length; i++)
        {
            char a;
            cin >> a;
            binNums[i] = a == '1' ? 1 : 0;
        }
        solve(binNums);
        binNums.clear();
    }
    return 0;
}