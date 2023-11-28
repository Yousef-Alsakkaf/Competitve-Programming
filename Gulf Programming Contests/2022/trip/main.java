import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;
import java.io.*;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("trip.in"));
        FileWriter write = new FileWriter(new File("trip.answer"));
        String numberOfCases = scan.nextLine();
        String result = "";

        for (int i = 0; i < Integer.parseInt(numberOfCases); i++) {
            String numberOfCountries = scan.nextLine();
            ArrayList<ArrayList<Integer>> allLists = new ArrayList<ArrayList<Integer>>();

            for (int j = 0; j < Integer.parseInt(numberOfCountries); j++) {
                String line = scan.nextLine();
                ArrayList<Integer> list = getList(line);

                if (!list.isEmpty()) {
                    allLists.add(list);
                }
            }

            ArrayList<Integer> smallestList = allLists.get(0);
            ArrayList<Integer> sharedCountries = new ArrayList<Integer>();

            for (int z = 0; z < smallestList.size(); z++) {
                boolean includedInAll = true;
                for (int a = 1; a < allLists.size(); a++) {
                    ArrayList<Integer> selectedList = allLists.get(a);
                    if (!selectedList.contains(smallestList.get(z))) {
                        includedInAll = false;
                    }
                }

                if (includedInAll) {
                    sharedCountries.add(smallestList.get(z));
                }
            }

            result += (i + 1) + ". ";

            if(sharedCountries.isEmpty()) {
                result += "No Trip";
            } else {
                String joinedString = "";
                Collections.sort(sharedCountries);
                for(int c = 0; c < sharedCountries.size(); c++) {
                    joinedString+= sharedCountries.get(c);
                    if(c != sharedCountries.size() - 1) {
                        joinedString += ",";
                    }
                }
                result += joinedString;
            }

            result += "\n";

        }

        write.write(result);
        scan.close();
        write.close();
    }

    public static ArrayList<Integer> getList(String input) {
        ArrayList<Integer> list = new ArrayList<Integer>();

        String[] splittedInput = input.split(" ");

        for (int i = 1; i < splittedInput.length; i++) {
            list.add(Integer.parseInt(splittedInput[i]));
        }

        return list;
    }
}
