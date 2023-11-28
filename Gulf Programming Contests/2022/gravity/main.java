import java.io.FileWriter;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.Scanner;
import java.io.*;

public class main {
    public static void main(String[] args) throws IOException{
        Scanner scan = new Scanner(new File("gravity.in"));
        FileWriter write = new FileWriter("gravity.answer");
        Integer numberOfTestCases = scan.nextInt();
        String result = "";

        for(int i = 0; i < numberOfTestCases; i++) {
            int mass = scan.nextInt();
            String planetName = scan.next();
            double gravityFactor = scan.nextDouble();
            DecimalFormat df1 = new DecimalFormat("0.0");
            DecimalFormat df2 = new DecimalFormat("0");

            result += "Earth ";
            result += df2.format(calculateWeight(mass, 10.0)) + "N ";
            result += planetName + " ";
            BigDecimal decimalVar = new BigDecimal(calculateWeight(mass, gravityFactor));
            BigDecimal roundedDecimal = decimalVar.setScale(2, RoundingMode.HALF_UP);
            result += df1.format(roundedDecimal) + "N";
            result += "\n";
        }

        System.out.println();

        write.write(result);
        scan.close();
        write.close();
    }

    public static double calculateWeight(int mass, double gravityFactor) {
        return mass * gravityFactor;
    }
}
