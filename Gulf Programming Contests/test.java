import java.util.Arrays;
import java.util.HashMap;

public class test {
    public static void main(String[] args) {
        System.out.println(findN(10));
    }

    public static int findN(int n) {
        int counter = 0;

        while(n != 0) {
            if(n % 2 == 0) {
                n/=2;
            } else {
                n--;
            }

            counter++;
        }

        return counter;
    }
}

// 2553432