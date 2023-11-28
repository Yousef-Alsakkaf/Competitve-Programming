import java.util.Scanner;

public class Stones{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        String input = scan.next();
        int counter = 0;
        char [] chars = new char[size];
        for(int i = 0; i < chars.length; i++){
            chars[i] = input.charAt(i);
        }
        for(int i = 1; i < chars.length; i++){
            if(chars[i] == chars[i - 1]){
                counter++;
            }
        }
        System.out.println(counter);
    }
}