#include <iostream>
#include <string>
using namespace std;
string print(int x)
{
    if(x < 10) return "0" + to_string(x);
    else return to_string(x);
}
int main()
{
    int h, m, s;
    char r;
    string str;

    cin >> h >> r >> m >> r >> s >> str;

    if(str == "PM" && h != 12) h += 12;
    else if (str == "AM" && h == 12) h = (h + 12) % 24;

    cout << print(h)<< ":" << print(m) << ":" << print(s);
    return 0;
}