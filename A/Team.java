import java.util.Scanner;
public class Team {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        int counter = 0;
        for(int i = 0; i < num; i++){
            int sure = 0;
            for(int j = 0; j < 3; j++){
                if(scan.nextInt() == 1) sure += 1;
            }
            if(sure > 1) counter++;
        }
        System.out.println(counter);
    }
}
