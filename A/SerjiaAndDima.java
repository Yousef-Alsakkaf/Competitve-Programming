import java.util.Arrays;
import java.util.Scanner;

public class SerjiaAndDima {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int [] cards = new int[size];    
        for(int i = 0; i < cards.length; i++){
            cards[i] = scan.nextInt();
        }
        int left = 0, right = cards.length - 1;
        boolean isSerjiaTurn = true;
        int serja = 0, dima = 0;
        while(left <= right){
            int plus = 0;
            if(cards[left] <= cards[right]){
                plus = cards[right];
                right--;
            }
            else{
                plus = cards[left];
                left++;
            }
            if(isSerjiaTurn){
                serja += plus;
            } else{
                dima += plus;
            }
            isSerjiaTurn = !isSerjiaTurn;
        }
        System.out.println(serja + " " + dima);
    }
}
