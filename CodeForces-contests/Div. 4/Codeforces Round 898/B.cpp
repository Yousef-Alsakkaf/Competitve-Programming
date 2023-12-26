#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    vector<int> arr;
    string result = "";
    while(T--)
    {
        int n;
        cin >> n;
        arr.resize(n);
        int min = 10;
        for(int i = 0; i < n; i++)
        {
            cin >> arr[i];
            if(min > arr[i])
            {
                min = arr[i];
            }
        }
        int product = 1;
        int found = false;
        for(int i = 0; i < n; i++)
        {
            if(arr[i] == min && !found)
            {
                product *= (arr[i] + 1);
                found = true;
            }
            else
            {
                product *= arr[i];
            }
        }
        result += to_string(product)+ "\n";       
    }
    cout << result;
    return 0;
}