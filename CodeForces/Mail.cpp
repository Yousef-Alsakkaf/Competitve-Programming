#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int nums;
    cin >> nums;

    vector<int> numbers;
    for(int i = 0; i < nums; i++)
    {
        int a;
        cin >> a;
        numbers.push_back(a);
    }
    for(int i = 0; i < numbers.size(); i++)
    {
        int minimum, maximum;
        if(i == 0)
        {
            minimum = abs(numbers[i] - numbers[i + 1]);
            maximum = (numbers[numbers.size() - 1]) - numbers[i];
        }
        else if(i == numbers.size() - 1)
        {
            minimum = numbers[i] - numbers[i - 1];
            maximum = numbers[i] - numbers[0];
        }
        else
        {
            int min1 = abs(numbers[i] - numbers[i + 1]);
            int min2 = abs(numbers[i] - numbers[i - 1]);
            minimum = min(min1, min2);
            int max1 = (numbers[numbers.size() - 1]) - numbers[i];
            int max2 = numbers[i] - numbers[0];
            maximum = max(max1, max2);
        }
        cout << minimum  << " " << maximum << endl;
    }
    return 0;
}
