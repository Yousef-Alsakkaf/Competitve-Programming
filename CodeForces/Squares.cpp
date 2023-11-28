#include <iostream>
#include <vector>
using namespace std;

int main(){
    int cal1,cal2,cal3,cal4,sum=0;
    cin >> cal1 >> cal2 >> cal3 >> cal4;
    string s;
    cin >> s;
    for(int i = 0;i<s.length();i++)
    {
        switch (s[i])
        {
            case '1' :
                sum += cal1;
                break;
            case '2' :
                sum += cal2;
                break;
            case '3' :
                sum += cal3;
                break;
            case '4' :
                sum += cal4;
                break;
        }
    }
    cout << sum << "\n";
    return 0;
}