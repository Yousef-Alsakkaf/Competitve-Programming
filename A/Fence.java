import java.util.Scanner;

public class Fence{
    public static void main(String [] args){
        Scanner scan = new Scanner(System.in);
        int numOfFriends = scan.nextInt();
        int Height = scan.nextInt();
        
        int res = 0;
        for(int i = 0; i < numOfFriends; i++){
            if(scan.nextInt() > Height){
                res += 2;
            } else{
                res += 1;
            }
        }
        System.out.println(res);
    }
}