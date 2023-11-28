import java.util.*;
import java.io.*;

public class areej {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("areej.in"));
        String line = scan.nextLine();
        String[] arguments = line.split(" ");
        long testCases = Integer.parseInt(arguments[0]);
        int testItems = Integer.parseInt(arguments[1]);
        String result = "";

        try {
            while (testCases != 0) {
                HashMap<String, Integer> map = new HashMap<String, Integer>();

                for (int i = 0; i < testCases; i++) {
                    int nOfLines = Integer.parseInt(scan.nextLine());
                    String[] array = new String[testItems];
                    for (int j = 0; j < nOfLines; j++) {
                        String value = scan.nextLine();
                        if (!map.containsKey(value)) {
                            map.put(value, 1);
                        } else {
                            int temp = map.get(value);
                            map.put(value, temp + 1);
                        }

                        sortArrayMax(map, array);
                    }

                    System.out.println(array[findFirstNonNull(array)]);
                    System.out.println(Arrays.toString(array));
                    result += array[findFirstNonNull(array)];
                    result += "\n";
                    map.clear();
                }
                result += "\n";

                line = scan.nextLine();
                arguments = line.split(" ");
                testCases = Integer.parseInt(arguments[0]);
                testItems =  Integer.parseInt(arguments[1]);
            }
        } catch (NoSuchElementException e) {

        }

        FileWriter write = new FileWriter("areej.answer");
        write.write(result);
        write.close();
    }

    public static void sortArrayMax(HashMap<String, Integer> map, String[] result) {
        Set<String> array = map.keySet();

        for (String s : array) {
            if (!hasValue(result, s)) {
                appendArrayToValue(result, s);
            }
        }

        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result.length; j++) {
                if (i == j)
                    continue;
                if (result[i] == null || result[j] == null)
                    continue;
                if (map.get(result[i]) < map.get(result[j])) {
                    String tempValue = result[i];
                    result[i] = result[j];
                    result[j] = tempValue;
                }
            }
        }
    }

    public static boolean hasValue(String[] arr, String check) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == null)
                continue;
            if (arr[i].equals(check))
                return true;
        }

        return false;
    }

    public static void appendArrayToValue(String[] arr, String value) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == null) {
                arr[i] = value;
                break;
            }
        }
    }

    public static int findFirstNonNull(String[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == null) {
                return i - 1;
            }
        }

        return arr.length - 1;
    }


}
