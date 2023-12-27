#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;

    int arr[3];
    while(T--)
    {
        cin >> arr[0] >> arr[1] >> arr[2];
        bool found = false;
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 3; j++)
            {
                if(arr[i] + arr[j] >= 10 && i != j)
                {
                    found = true;
                    break;
                }
            }
        }
        if(found) cout << "YES\n";
        else cout << "NO\n";

    }
    return 0;
}