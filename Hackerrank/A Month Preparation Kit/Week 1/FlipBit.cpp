#include <iostream>
#include <string>
using namespace std;

string to_binary(long long num)
{
    if(num == 0) return "0";

    string binary = "";

    while(num > 0)
    {
        binary = to_string(num % 2) + binary;
        num /= 2;
    }

    return binary;
}

string complete(string num)
{
    while(num.length() < 32)
    {
        num = "0" + num;
    }
    return num;
}

void flip(string& binaryNum)  // Fix the function name here
{
    for(int i = 0; i < binaryNum.length(); i++)
    {
        if(binaryNum[i] == '0') binaryNum[i] = '1';
        else binaryNum[i] = '0';
    }
}

unsigned int to_decimal(const string& binary_num)
{
    unsigned int decimal_num = 0;
    unsigned int power = 1;

    for (int i = binary_num.length() - 1; i >= 0; --i)
    {
        if (binary_num[i] == '1')
        {
            decimal_num += power;
        }

        power *= 2;
    }

    return decimal_num;
}

int main()
{
    int T;
    cin >> T;

    while(T--)
    {
        long long num;
        cin >> num;
        string binaryNum = to_binary(num);
        binaryNum = complete(binaryNum);
        flip(binaryNum); 
        cout << to_decimal(binaryNum) << endl;
    }
    return 0;
}
