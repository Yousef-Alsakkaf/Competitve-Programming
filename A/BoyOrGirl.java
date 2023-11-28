import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class BoyOrGirl {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        Map <Character, Integer> map = new HashMap<>();
        for(int i = 0; i < str.length(); i++){
            map.put(str.charAt(i), map.getOrDefault(map, 0) + 1);
        }
        int counter = 0;
        for(Map.Entry<Character, Integer> entry : map.entrySet()){
            if(entry.getValue() == 1){
                counter += 1;
            }
        }
        System.out.println(counter % 2 == 0 ? "CHAT WITH HER!":"IGNORE HIM!");
    }
}
