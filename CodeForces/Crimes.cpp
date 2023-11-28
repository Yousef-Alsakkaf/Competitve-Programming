#include <iostream>
using namespace std;

int main(){
    int num;
    cin >> num;

    int ans = 0;
    int numOfOficcers = 0;
    for(int i = 0; i < num; i++){
        int a;
        cin >> a;

        if(a != -1){
            numOfOficcers += a;
        }
        else if(a == -1 && numOfOficcers == 0){
            ans++;
        }
        else if(a == -1 && numOfOficcers > 0){
            numOfOficcers--;
        }
    }
    cout << ans;
    return 0;
}