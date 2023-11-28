#include <iostream>
using namespace std;
int main(){
    int num;
    string prev, curr;
    cin >> num >> prev;

    int groups = 0;
    for(int i = 0; i < num - 1; i++){
        cin >> curr;
        if(prev != curr){
            groups++;
        }
        prev = curr;
    }
    groups++;
    cout << groups;
}