import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HorseShoe {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Map <Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < 4; i++){
            int index = scan.nextInt();
            map.put(index, map.getOrDefault(index, 0) + 1);
        }
        int count = 0;
        for(Map.Entry<Integer, Integer> entrymap: map.entrySet()){
            // if(entrymap.getValue() > 1){
            count += 1;
            // }
        }
        System.out.println((4 - count));
    }
}
