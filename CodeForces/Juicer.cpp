#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int nums, max, d;
    cin >> nums >> max >> d;
    int sum = 0, counter = 0;
    for(int i = 0; i < nums; i++)
    {
        int a;
        cin >> a;

        if(a > max)
        {
            continue;
        }

        sum+=a;
        if(sum > d)
        {
            sum = 0;
            counter++;
        }
    }
    cout << counter;
    return 0;
}