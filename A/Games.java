import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Games {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        int [] nums = new int[size];
        Map <Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < size; i++){
            nums[i] = scan.nextInt();
            int guest = scan.nextInt();
            map.put(guest, map.getOrDefault(guest, 0) + 1);
        }
        int counter = 0;
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                counter += map.get(nums[i]);
            }
        }
        System.out.println(counter);
    }
}
