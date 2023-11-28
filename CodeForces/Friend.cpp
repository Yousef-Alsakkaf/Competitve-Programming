#include <iostream>

int main()
{
    int num;
    std::string str;
    std::cin >> num >> str;

    int D = 0, A = 0;
    for (int i = 0; i < num; i++)
    {
        if (str.at(i) == 'A')
        {
            A++;
        }
        else
        {
            D++;
        }
    }
    if (A > D)
    {
        std::cout << "Anton";
    }
    else if (D > A)
    {
        std::cout << "Danik";
    }
    else
    {
        std::cout << "Friendship";
    }
    return 0;
}