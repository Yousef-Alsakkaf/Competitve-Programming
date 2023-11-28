#include <iostream>
#include <cmath>
int main(){
    int Iindex, Jindex;
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            int a;
            std::cin >> a;
            if(a == 1){
                Iindex = i;
                Jindex = j;
            }
        }
    }
    int ans = abs(2-Iindex) + abs(2 - Jindex);
    std::cout << ans;
}