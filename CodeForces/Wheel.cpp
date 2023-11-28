#include <iostream>
using namespace std;

int main(){
    string s;
    cin >> s;

    int character = 'a';
    int counter = 0;
    for(int i = 0; i < s.length(); i++){
        int colockwise = (character - s[i] + 26) % 26;
        int other = (s[i] - character + 26) % 26;
        counter += min(colockwise, other);
        character = s[i];
    }
    cout << counter;
    return 0;
}