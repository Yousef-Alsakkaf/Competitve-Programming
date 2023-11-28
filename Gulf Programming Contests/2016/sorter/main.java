import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

class main {
    public static void main(String[] args) throws IOException {
        BufferedReader file = new BufferedReader(new FileReader("sorter.in"));
        String nOfTestCases = file.readLine();
        String result = "";

        for (int i = 0; i < Integer.parseInt(nOfTestCases); i++) {
            String line = file.readLine();
            System.out.println(line);
            String[] rotatedString = getRotationArray(line);
            Arrays.sort(rotatedString);
                        System.out.println(findIndex(rotatedString, line));
            result += findIndex(rotatedString, line) + "\n";
        }

        FileWriter write = new FileWriter(new File("sorter.answer"));

        write.write(result);

        write.close();
        file.close();
    }

    public static String[] getRotationArray(String input) {
        String[] arr = new String[input.length()];
        arr[0] = input;

        for (int i = 1; i < arr.length; i++) {
            String[] splittedWord = arr[i - 1].split("");
            String result = "";

            for (int j = 1; j < splittedWord.length; j++) {
                result += splittedWord[j];
            }

            result += splittedWord[0];

            arr[i] = result;
        }

        return arr;
    }

    public static int findIndex(String[] arr, String input) {
        int result = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(input))
                result = i;
        }

        return result;
    }
}