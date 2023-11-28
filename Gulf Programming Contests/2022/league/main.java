import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("league.in"));
        FileWriter write = new FileWriter(new File("league.answer"));
        int nOfCases = scan.nextInt();
        String result = "";

        for(int i = 0; i < nOfCases; i++) {
            int numberOfDivisions = scan.nextInt();
            int numberOfSeasons = scan.nextInt();
            int numberOfPromotions = scan.nextInt();
            int numberOfRelegations = scan.nextInt();
            result += (i + 1) + ". " + calculateDivision(numberOfDivisions, numberOfSeasons, numberOfPromotions, numberOfRelegations) + "\n";
        }

        write.write(result);
        write.close();
        scan.close();
    }

    public static int calculateDivision(int numberOfDivisions, int numberOfSeasons, int numberOfPromotions, int numberOfRelegations) {
        int difference = numberOfPromotions - numberOfRelegations;
        int calculation = numberOfDivisions - difference;

        if(calculation > numberOfDivisions) {
            return numberOfDivisions;
        } else if(calculation < 1) {
            return 1;
        } else {
            return calculation;
        }
    }
}
