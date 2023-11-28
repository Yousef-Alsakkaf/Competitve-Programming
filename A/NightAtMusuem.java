import java.util.Scanner;

public class NightAtMusuem {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int character = 'a';
        int counter = 0;
        for(int i = 0; i < s.length(); i++){
            int target = s.charAt(i);
            int clockwiseRotate = (target - character + 26) % 26;
            int theOthterOne = (character - target + 26) % 26;
            counter += Math.min(clockwiseRotate, theOthterOne);

            character = target;
        }
        System.out.println(counter);
    }
}
