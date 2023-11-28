#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int num;
    cin >> num;

    vector<int> nums(num, 0);
    for(int i = 0; i < num; i++)
    {
        int a;
        cin >> a;
        nums[a - 1] = i + 1;
    }
    for(int i = 0; i < num; i++)
    {
        cout << nums[i] << " ";
    }
    return 0;
}