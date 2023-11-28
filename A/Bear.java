import java.util.Scanner;;
public class Bear {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int Limak = scan.nextInt();
        int Bob = scan.nextInt();
        
        int res = 0;
        while(Limak <= Bob){
            Limak *= 3;
            Bob *= 2;
            res += 1;
        }
        System.out.println(res);
    }
}
