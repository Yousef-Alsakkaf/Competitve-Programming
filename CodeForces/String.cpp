#include <iostream>

int main()
{
    std::string s1, s2;
    std::cin >> s1 >> s2;

    int n = s1.length();
    std::string x, y;
    for (int i = 0; i < n; i++)
    {
        char a = toupper(s1.at(i));
        char b = toupper(s2.at(i));
        x += a;
        y += b;
    }
    if (x == y)
    {
        std::cout << 0;
    }
    else if (x > y)
    {
        std::cout << 1;
    }
    else
    {
        std::cout << -1;
    }
}