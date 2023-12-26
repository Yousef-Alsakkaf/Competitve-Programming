#include <iostream> 
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    int arr[10][10] = {
    {1,1,1,1,1,1,1,1,1,1},
	{1,2,2,2,2,2,2,2,2,1},
	{1,2,3,3,3,3,3,3,2,1},
	{1,2,3,4,4,4,4,3,2,1},
	{1,2,3,4,5,5,4,3,2,1},
	{1,2,3,4,5,5,4,3,2,1},
	{1,2,3,4,4,4,4,3,2,1},
	{1,2,3,3,3,3,3,3,2,1},
	{1,2,2,2,2,2,2,2,2,1},
	{1,1,1,1,1,1,1,1,1,1}
    };
    string result = "";
    while(T--)
    {
        int counter = 0;
        for(int i = 0; i < 10; i++)
        {
            for(int j = 0; j < 10; j++)
            {
                char a;
                cin >> a;

                if(a == 'X')
                {
                    counter += arr[i][j];
                }
            }
        }
        result += to_string(counter) + "\n";
    }
    cout << result;
    return 0;
}