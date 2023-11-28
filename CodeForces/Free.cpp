#include <iostream>
using namespace std;

int main()
{
    long long days, sum;
    cin >> days >> sum;

    int counter = 0;
    for(int i = 0; i < days; i++)
    {
        string sign;
        long num;
        cin >> sign >> num;
        if(sign == "+")
        {
            sum += num;
        }
        else
        {
            if(sum - num < 0)
            {
                counter++;
            }
            else
            {
                sum -= num;
            }
        }
    }
    cout << sum << " "<< counter;
    return 0;
}