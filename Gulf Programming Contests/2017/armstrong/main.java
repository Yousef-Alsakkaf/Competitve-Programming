import java.io.IOException;
import java.util.Scanner;
import java.io.*;
import java.util.*;

public class main {
    public static void main(String[] args) throws IOException {

        Scanner scan = new Scanner(new File("armstrong.in"));
        FileWriter file = new FileWriter(new File("armstrong.answer"));
        int nOfTestCases = scan.nextInt();
        String result = "";

        for(int i = 0; i < nOfTestCases; i++) {
            int num = scan.nextInt();

            boolean res = calculate(num);

            result+= (i + 1) + ". " + (res ? "yes" : "no");
            result+= "\n";
        }

        file.write(result);
        file.close();
        scan.close();
    }

    public static boolean calculate(long input) {
        String in = input + "";
        long total = 0;

        for(int i = 0; i < in.length(); i++) {
            int num = Integer.parseInt(in.charAt(i)+"");
            total+= Math.pow(num, in.length());
        }

        if(total == input) {
            return true;
        } else {
            return false;
        }
    }


}
