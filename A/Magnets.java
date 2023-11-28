import java.util.Scanner;

public class Magnets{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int [] magnets = new int[size];
        int counter = 1;
        for(int i = 0; i < magnets.length; i++){
            magnets[i]=scan.nextInt();
            if(i >= 1 && magnets[i- 1] != magnets[i]){
                counter++;
            }
        }
        System.out.println(counter);
    }
}