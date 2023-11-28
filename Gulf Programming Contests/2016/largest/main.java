import java.io.File;
import java.io.FileWriter;
import java.util.*;

public class main {
    public static void main(String[] args) throws Exception{
        File khra = new File("largest.in");
        FileWriter write = new FileWriter("largest.answer");
        Scanner scanner = new Scanner(khra);
        int k = scanner.nextInt(); 
        String res = "";

        for (int i = 0; i < k; i++) {
            int n = scanner.nextInt(); 
            Integer[] numbers = new Integer[n];
            

            for (int j = 0; j < n; j++) {
                numbers[j] = scanner.nextInt();
            }
            

            String result = "";

            Arrays.sort(numbers, (n1, n2) -> compareValues(n1, n2));

            for(int b = 0; b < numbers.length; b++) {
                result = numbers[b] + result;
            }
            // System.out.println(Arrays.toString(numbers) + " " +result);

            res += result + "\n";
        }

        write.write(res);


        scanner.close();
        write.close();
    }

    public static int compareValues(int n1, int n2) {
        String n1Max = "" + n1;
        int n1MaxNum = getNineNineValue(n1Max.length());
        String n2Max = "" + n2;
        int n2MaxNum = getNineNineValue(n2Max.length());

        double n1Diff = (double) n1 / n1MaxNum;
        double n2Diff = (double) n2 / n2MaxNum;
        
        if(n2Diff > n1Diff) {
            return -1;
        } else if(n2Diff == n1Diff) {
            return 0;
        } else {
            return 1;
        }
    }

    public static int getNineNineValue(int length) {
        String result = "";

        for (int i = 0; i < length; i++) {
            result += "9";
        }

        return Integer.parseInt(result);
    }

}

// [333, 3332] 3332333
// [0.3333333333, 0.3332333233]