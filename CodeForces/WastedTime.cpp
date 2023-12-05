#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

int main()
{
    int n, k; // the number of points - the number of papers
    cin >> n >> k;
    vector<vector<int>> pairs(n);
    double sum = 0;
    for(int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        pairs[i].push_back(x);
        pairs[i].push_back(y);
        if(i != 0)
        {
            double distance = sqrt(pow(x - pairs[i -1][0], 2) + pow(y - pairs[i - 1][1], 2));
            sum += distance;
        }
    }
    sum = (sum / 50) * k;
    cout << setprecision(10)<< sum;
}