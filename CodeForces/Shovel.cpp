#include <iostream>
using namespace std;

int main(){
    int coins, curles;
    cin >> coins;
    cin >> curles;
    int counter = 1;
    int temp = coins;
    while(temp % 10 != 0 && temp % 10 != curles){
        counter++;
        temp = coins * counter;
    }
    cout  <<  counter << endl;
    return 0;
}