#include <iostream>
#include <vector>
using namespace std;
int T, kills, x, y;
int main()
{
    cin >> T;

   vector<int> nums(T + 2);
    for(int i = 1; i < nums.size() - 1; i++)
    {
        cin >> nums[i];
    }
    cin >> kills;
    for(int i = 0; i < kills; i++)
    {
        cin >> x >> y;
        nums[x+1] = nums[x+1] + (nums[x] - y);
        nums[x - 1] = nums[x - 1] + y - 1;
        nums[x] = 0;
    }

    for(int i = 1; i < nums.size() - 1;i++)
    {
        cout <<nums[i] << endl;
    } 
    return 0;
}