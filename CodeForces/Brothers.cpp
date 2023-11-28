#include <iostream>

int main()
{
    int Limak, Bob;
    std::cin >> Limak >>Bob;

    int counter = 0;
    while(Limak <= Bob)
    {
        Limak *= 3;
        Bob *= 2;
        counter++;
    }
    std::cout << counter;
    return 0;
}