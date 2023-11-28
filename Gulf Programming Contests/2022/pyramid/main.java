import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

public class main {
    public static void main(String[] args) throws IOException{
        char[] getThirdPyramid133;
        System.out.println(getThirdPyramid(33));
        // Scanner scan = new Scanner(new File("pyramid.in"));
        // FileWriter file = new FileWriter(new File("pyramid.answer"));
        // String result = "";




        // file.write(file);
        // scan.close();
        // file.close();
    }

    public static long getThirdPyramid(int n) {
        long result = 0;

        while (n > 0) {
            result += n;
            n--;
        }

        return result;
    }

    public static long getFourthPyramid(int n) {
        return getThirdPyramid(n) + getThirdPyramid(n - 1);
    }

    public static long getSixthPyramid(int n) {
        long result = 0;
        long base = 2 * n - 1;

        while (base >= n) {
            if (base == (2 * n - 1)) {
                result += base;
            } else {
                result += base * 2;
            }
            base--;
        }

        return result;
    }
}
