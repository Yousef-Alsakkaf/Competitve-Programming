#include <iostream>
using namespace std;
bool isPrime(int n)
{
    if(n == 1)
    {
        return false;
    }
    for(int i = 2; i * i <= n; i++)
    {
        if(n % i == 0)
        {
            return false;
        }
    }
    return true;
}
int main()
{
    int n, m;
    cin >> n >> m;
    int nextNum = n + 1;
    while(!isPrime(nextNum))
    {
        nextNum++;
    }
    if(m == nextNum)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}