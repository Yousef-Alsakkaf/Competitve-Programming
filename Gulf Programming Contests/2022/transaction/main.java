import java.io.*;
import java.util.*;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("transaction.in"));
        FileWriter file = new FileWriter(new File("transaction.answer"));
        String result = "";
        int line = scan.nextInt();

        while (line != 0) {
            ArrayList<String> arr = new ArrayList<String>();
            for (int i = 0; i < line; i++) {
                String transaction = scan.next();
                arr.add(transaction);
            }
            int s = scan.nextInt();
            int k = scan.nextInt();
            String uniqueCharacters = getListOfUniqueCharacters(arr);
            ArrayList<String> arr2 = new ArrayList<String>();
            generateCombinationsRecursive(k, s, uniqueCharacters, "", arr2, -1);
            HashMap<String, Integer> map = new HashMap<String, Integer>();

            for (String input : arr) {
                for (int i = 0; i < arr2.size(); i++) {
                    String combination = arr2.get(i);
                    boolean allIn = true;
                    for (int j = 0; j < combination.length(); j++) {
                        if (!input.contains(combination.charAt(j) + "")) {
                           allIn = false;
                        }
                    }
                    if (allIn) {
                        map.put(combination, map.getOrDefault(combination, 0) + 1);
                    }
                }
            }

            int counter = 0;

            for(int item: map.values()) {
                if(item >= s) {
                    counter++;
                }
            }

            result += counter;
            result += "\n";
            line = scan.nextInt();
        }
        System.out.println(result);

        file.write(result);
        scan.close();
        file.close();
    }

    public static String getListOfUniqueCharacters(ArrayList<String> arr) {
        String result = "";

        for (int i = 0; i < arr.size(); i++) {
            String str = arr.get(i);
            for (int j = 0; j < str.length(); j++) {
                if (!result.contains(str.charAt(j) + "")) {
                    result += str.charAt(j);
                }
            }
        }

        return result;
    }

    public static void generateCombinationsRecursive(int k, int s, String characters, String currentCombination,
            ArrayList<String> combinations, int counter) {
        if (k == 0) {
            combinations.add(currentCombination);
            return;
        }

        for (int i = counter + 1; i < characters.length(); i++) {
            char character = characters.charAt(i);
            generateCombinationsRecursive(k - 1, s, characters, currentCombination + character, combinations, i);
        }
    }

}
