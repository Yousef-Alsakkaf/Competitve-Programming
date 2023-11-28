import java.util.*;
import java.io.*;

public class main {
    public static void main(String[] args) {
        BufferedReader reader;
        String result = "";

        try {
            reader = new BufferedReader(new FileReader("palindrome.in"));
            String line = reader.readLine();

            while (line != null && !line.equals("0 0")) {
                String num = line.split(" ")[0];
                String base = line.split(" ")[1];
                boolean checkIfPalindrome = isPalindrome(convertBase(Integer.parseInt(num),
                        Integer.parseInt(base)));
                String transform = checkIfPalindrome ? "Yes" : "No";
                result += transform + "\n";

                line = reader.readLine();
            }

            FileWriter myWriter = new FileWriter("palindrome.answer");
            myWriter.write(result);

            myWriter.close();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String[] convertBase(int number, int base) {
        String result = "";

        while (number != 0) {
            result += (number % base) + ",";
            number /= base;
        }

        return result.split(",");
    }

    public static boolean isPalindrome(String[] input) {
        boolean result = true;

        for (int i = 0, j = input.length - 1; i < input.length; i++, j--) {
            if (!input[i].equals(input[j])) {
                result = false;
            }
        }

        return result;
    }
}
