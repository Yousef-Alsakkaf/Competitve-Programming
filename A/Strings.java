import java.util.Scanner;

public class Strings {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String first = scan.next().toLowerCase().trim();
        String second = scan.next().toLowerCase().trim();
        int res = first.compareTo(second);
        System.out.println(res == 0 ? 0 : res > 0 ? 1 : -1);
    }
}
