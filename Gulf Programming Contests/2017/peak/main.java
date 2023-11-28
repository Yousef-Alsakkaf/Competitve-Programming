import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.io.*;

public class main {

    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("peak.in"));
        FileWriter file = new FileWriter("peak.answer");
        String result = "";
        int nOfCases = scan.nextInt();

        for (int i = 0; i < nOfCases; i++) {
            int nOfEmails = scan.nextInt();
            int lengthOfPointer = scan.nextInt();
            ArrayList<Integer> arr = new ArrayList<Integer>();
            int max = Integer.MIN_VALUE;

            for (int j = 0; j < nOfEmails; j++) {
                int num = scan.nextInt();
                arr.add(num);
                max = Math.max(max, num);
            }

            int[] arr2 = new int[max];

            for (int j = 0; j < arr.size(); j++) {
                arr2[arr.get(j) - 1]++;
            }

            int maxValue = 0;
            int maxInterval = 0;
            int p1 = 0;
            int p2 = lengthOfPointer - 1;

            for (int j = 0; j < lengthOfPointer; j++) { // Fill up first pointer
                maxInterval += arr2[j];
                maxValue = Math.max(maxInterval, maxValue);
            }

            for (int j = 1, k = lengthOfPointer; j < arr2.length - lengthOfPointer +1; j++, k++) {
                maxInterval -= arr2[p1];
                p1 = j;
                p2 = k;
                maxInterval += arr2[p2];

                maxValue = Math.max(maxInterval, maxValue);
            }

            result += (i + 1) + ". " + maxValue;
            result+= "\n";

        }

        file.write(result);
        file.close();
        scan.close();
    }

}
