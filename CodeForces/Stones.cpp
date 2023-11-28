#include <iostream>
using namespace std;
int main(){
    int s;
    cin >> s;

    string str;
    cin >> str;

    int counter = 0;
    for(int i = 1; i < s; i++){
        if(str.at(i) == str.at(i - 1)){
            counter++;
        }
    }
    cout << counter;
    return 0;
}