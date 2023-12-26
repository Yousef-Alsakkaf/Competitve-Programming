#include <iostream>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    string result = "";
    while(T--)
    {
        long long n, k;
        cin >> n >> k;

        string str;
        cin >> str;
        int i = 0, j = i + k -1;
        int counter = 0;
        while(i < n)
        {
            if(str[i] != 'B')
            {
                i++;
                j++;
            }
            else
            {
                counter++;
                i = j + 1;
                j = i + k - 1;
            }
        }
        result += to_string(counter) + "\n";
    }
    cout << result;
    return 0;
}