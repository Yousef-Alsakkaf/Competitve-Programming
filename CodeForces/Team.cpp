#include <iostream>

int main(){
    int num;
    int counter = 0;
    std::cin >> num;
    for(int i = 0; i < num; i++){
        int a, b, c;
        std::cin >> a >> b >> c;
    if((a + b +c) > 1)
    {   
      //  std::cout << "These are the values: " << a << b <<c <<std::endl;
        counter++;
    }
    }
    std::cout << counter;
    return 0;
}