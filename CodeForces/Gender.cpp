#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    unordered_map<char, int> myMap;
    string word;
    getline(cin, word);  // Use getline to read the entire input line

    for (int i = 0; i < word.length(); i++) {
        myMap[word.at(i)] += 1;
    }
    int counter = 0;

    for (const auto &pair : myMap) {
            counter += 1;
    }
    if (counter % 2 != 0) {
        cout << "IGNORE HIM!";
    } else {
        cout << "CHAT WITH HER!";
    }
    return 0;
}
