import java.util.Scanner;

public class Shovel {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int price = scan.nextInt();
        int coins = scan.nextInt();
        int counter = 1;
        int temp = price;
        while (temp % 10 != 0 && temp % 10 != coins) {
            counter++;
            temp += price;
        }

        System.out.println(counter);
    }
}
