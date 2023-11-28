import java.util.Scanner;

public class AntonAndDanic {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int A = 0;
        int D = 0;
        scan.nextInt();
        String str = scan.next();
        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) == 'A') A += 1;
            else D += 1;
        }
        System.out.println(A > D ? "Anton": D > A? "Danik": "Friendship" );
    }
}
