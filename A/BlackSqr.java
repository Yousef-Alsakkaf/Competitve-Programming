import java.util.Scanner;

public class BlackSqr {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int [] nums = new int[4];
        for(int i = 0; i < nums.length; i++){
            nums[i] = scan.nextInt();
        }
        String s = scan.next();
        int res = 0;
        for(int i = 0; i < s.length(); i++){
            res += nums[Integer.parseInt(s.charAt(i) + "") - 1];
        }
        System.out.println(res);
    }
}
