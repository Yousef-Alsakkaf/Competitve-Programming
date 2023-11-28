import java.util.Scanner;
public class Matrix {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int index = 0, jindex = 0;
        for(int i = 0; i < 5; i++){
            for(int j = 0; j < 5; j++){
                if(scan.nextInt() == 1){
                    index = i;
                    jindex = j;
                    break;
                }
            }
        }
        System.out.println(Math.abs(2 - index) + Math.abs(2-jindex));
    }
}
