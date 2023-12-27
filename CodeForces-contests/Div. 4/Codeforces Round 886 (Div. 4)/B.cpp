#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    
    pair<int, int> responses;
    while(T--)
    {
        int n;
        cin >> n;
        int max = 0;
        int counter = 1;
        int ind = 0;
        while(n--)
        {
            cin >> responses.first >> responses.second;
            if(responses.first <= 10 && responses.second > max)
            {
                max = responses.second;
                ind = counter;
            }
            counter++;
        }
        cout << ind << endl;
    }
    return 0;
}