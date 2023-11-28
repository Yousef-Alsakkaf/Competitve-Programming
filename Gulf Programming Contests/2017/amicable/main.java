import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.io.*;

public class main {
     public static void main(String[] args) throws IOException{
        Scanner scan = new Scanner(new File("amicable.in"));
        FileWriter file = new FileWriter("amicable.answer");
        int nOfTestCases = scan.nextInt();
        String result = "";

        for(int i =0; i < nOfTestCases; i++) {
            int num1 = scan.nextInt();
            int num2 = scan.nextInt();
            boolean result1 = calculate(num1, num2);
            boolean result2 = calculate(num2, num1);
            if(result1 && result2) {
                result+= num1 + " " + num2 + " are amicable numbers";
            } else {
                result+= num1 + " " + num2 + " are not amicable numbers";
            }

            result+= "\n";
        }

        System.out.println(result);

        file.write(result);
        file.close();
        scan.close();
     }

     public static boolean calculate(int num1, int num2) {
        int counter = 1;
        int total = 0;

        while(counter < num1) {


            if(isDecimal((double) num1/ counter)) {
                            System.out.println(num1 + " " + total + " " + counter);
                total+= counter;
                if(total > num2) {
                    return false;
                }

            }
            counter++;
        }

        if(total == num2) {
            return true;
        } else {
            return false;
        }
     }

     public static boolean isDecimal(double input) {
        return input == (int) input;
     }
}
