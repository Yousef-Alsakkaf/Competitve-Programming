import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class main {
    public static void main(String[] args) throws IOException{
        Scanner scan = new Scanner(new File("biplay.in"));
        FileWriter file = new FileWriter(new File("biplay.answer"));
        String result = "";
        String line = scan.nextLine();
        int counter = 1;
        String zeros = "000000000000000000000000";
        String ones = "111111111111111111111111";

        while (!line.equals("0 0")) {
            String[] argss = line.split(" ");
            int num1 = Integer.parseInt(argss[0]);
            int num2 = Integer.parseInt(argss[1]);
            int lowestNum = Integer.MAX_VALUE;

            int test1 = flipBinary(decimal2binary(num1), decimal2binary(num2));
            int test2 = flipBinary(zeros, decimal2binary(num2)) + 1;
            int test4 = flipBinary(ones, decimal2binary(num2)) + 1;
            lowestNum = Math.min(test2, test4);
            lowestNum = Math.min(test1, lowestNum);

            result += counter + ". ";
            result += lowestNum;
            result += "\n";
            line = scan.nextLine();
            counter++;
        }

        file.write(result);
        file.close();
        scan.close();
    }

    public static String decimal2binary(int n) {
        String result = "";

        while (n > 0) {
            boolean rem = n % 2 == 0;
            result = (rem ? "0" : "1") + result;
            n = n / 2;
        }

        if (result.length() < 24) {
            int difference = 24 - result.length();
            for (int i = 0; i < difference; i++) {
                result = "0" + result;
            }
        }

        return result;
    }

    public static int flipBinary(String a, String b) {
        int result = 0;

        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) != b.charAt(i)) {
                result++;
            }
        }

        return result;
    }
}
