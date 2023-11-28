import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner file = new Scanner(new File("guess.in"));
        FileWriter write = new FileWriter("guess.answer");
        int numberOfCases = file.nextInt();
        String result = "";

        for (int i = 0; i < numberOfCases; i++) {
            int x = file.nextInt();
            int y = file.nextInt();
            int z = file.nextInt();
            DecimalFormat df = new DecimalFormat("0.00");

            result += (i + 1) + ". " + df.format(calculateProbablity(x, y, z)) + "%\n";
        }

        write.write(result);
        write.close();
        file.close();
    }

    public static double calculateProbablity(int x, int y, int z) {
        try {
            int numbersToGuess = x - y;
            double probablityOfNumsToGuess = Math.pow(10, numbersToGuess);
            double numberOfGuesses = probablityOfNumsToGuess / z;
            double a = (double) 100 / numberOfGuesses;
            if (a > 100) {
                return 100.00;
            } else {
                return (double) 100 / numberOfGuesses;
            }
        } catch (ArithmeticException e) {
            return 0.0;
        }
    }
}
