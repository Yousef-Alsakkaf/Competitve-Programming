#include <iostream>
using namespace std;

bool arr[1000000];
int current = 0;
void solve(int x, int current2)
{
    for (int i = current2; i > 0; i--)
    {
        if (arr[i])
        {
            cout << i << " ";
            arr[i] = 0;
            current = i - 1;
        }
        else
        {
            break;
        }
    }
}
int main()
{
    int num;
    cin >> num;
    current = num;
    for (int i = 0; i < num; i++)
    {
        int x;
        cin >> x;
        arr[x] = 1;
        solve(x, current);
        cout << endl;
    }
    return 0;
}