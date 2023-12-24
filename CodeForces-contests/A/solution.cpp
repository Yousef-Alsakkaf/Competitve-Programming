#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

int main()
{
    int T; // number of test cases
    cin >> T;
    while(T--)
    {
        int size;
        cin >> size;
        unordered_set<int> x_set(size);
        unordered_set<int> y_set(size);
        for(int i = 0; i < size; i++)
        {
            int a, b;
            cin >> a >> b;
            x_set.insert(a);
            y_set.insert(b);
        }
        int counter = 0, isUp = 0, isDown = 0, isRight = 0, isLeft = 0;
        vector<int> xSet(x_set.begin(), x_set.end());
        vector<int> ySet(y_set.begin(), y_set.end());
        sort(xSet.begin(), xSet.end());
        sort(ySet.begin(), ySet.end());

        for(int i = 0; i < xSet.size(); i++)
        {
            if(xSet[i] < 0)
            {
                isLeft = 1;
            }
            if(xSet[i] > 0)
            {
                isRight = 1;
            }
        }
        for(int i = 0; i < ySet.size(); i++)
        {
            if(ySet[i] < 0)
            {
                isDown = 1;
            }
            if(ySet[i] > 0)
            {
                isUp = 1;
            }
        }
        if(isUp == 1)
        {
            counter++;
        }
        if(isDown == 1)
        {
            counter++;
        }
        if(isLeft == 1)
        {
            counter++;
        }
        if(isRight == 1)
        {
            counter++;
        }
        if(counter <= 3)
        {
            cout << "YES\n";
        }
        else
        {
            cout << "NO\n";
        }

    }
    return 0;
}