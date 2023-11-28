import java.util.Arrays;
import java.util.Scanner;

public class Cubes {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int [] columns = new int[scan.nextInt()];
        for(int i= 0; i < columns.length; i++){
            columns[i] = scan.nextInt();
        }
        Arrays.sort(columns);
        String res = "";
        for(int column : columns){
            res += column + " ";
        }
        System.out.println(res.trim());
    }
}
