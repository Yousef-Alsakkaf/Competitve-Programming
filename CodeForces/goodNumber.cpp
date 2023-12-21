#include <iostream>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    string str = "0123456789";
    int counter = 0, sum = 0;
    int found = -1;
    for (int i=0; i<n; i++)
    {
        string num;
        cin >> num;

        for(int j = 0; j <= k; j++)
        {
            found = num.find(str[j]);
            if(found != -1)
            {
                counter++;
                found = -1;
            }
        }
        if(counter >= k + 1) sum++;
        counter = 0;
    }
    cout << sum << endl;
    return 0;
}