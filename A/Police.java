import java.util.Scanner;

public class Police {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int [] nums = new int[size];
        for(int i = 0; i <  nums.length; i++){
            nums[i] = scan.nextInt();
        }
        int availableOfficers = 0;
        int res = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == -1 && availableOfficers == 0){
                res++;
            } else if(nums[i] == -1 && availableOfficers > 0 && res !=0){
                // res -= 1;
                availableOfficers--;
            } else{
                availableOfficers += nums[i];
            }
        }
        System.out.println(res);
    }
}
