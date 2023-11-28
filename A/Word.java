import java.util.Scanner;

public class Word {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s1 = scan.next();
        String s2 = s1.toLowerCase();
        
        int countC = 0;
        int countS = 0;
        for(int i = 0; i <  s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
                countC++;
            } else{
                countS++;
            }
        }
        if(countS >= countC){
            System.out.println(s2);
        } else{
            System.out.println(s1.toUpperCase());
        }
    }
}
