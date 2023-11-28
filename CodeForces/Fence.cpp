#include <iostream>

int main()
{
    int num, height;
    std::cin >> num >> height;
    int counter = 0;

    for (int i = 0; i < num; i++)
    {
        int a;
        std::cin >> a;

        if (a <= height)
        {
            counter++;
        }
        else
        {
            counter += 2;
        }
    }
    std::cout << counter;
    return 0;
}