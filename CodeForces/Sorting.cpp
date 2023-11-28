#include <iostream>
#include <list>
#include <vector>
using namespace std;
int main(){
    int num;
    cin >> num;
    vector <int> nums;
    for(int i = 0; i < num; i++){
        int a;
        cin >> a;
        nums.push_back(a);
    }
    int S = 0, D = 0;
    int left = 0, right = nums.size() - 1;
    int i = 0;
    while(left <= right){
        if(nums[right] >= nums[left]){
            if(i % 2 == 0){
                S += nums[right];
            }
            else
            {
                D += nums[right];
            }
            right--;
        }
        else{
            if(i % 2 == 0){
                S += nums[left];
            }
            else
            {
                D += nums[left];
            }
            left++;
        }
        i++;
    }
    cout << S << " " << D;
}