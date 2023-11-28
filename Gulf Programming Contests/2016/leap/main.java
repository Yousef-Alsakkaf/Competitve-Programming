import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class main {
    public static void main(String[] args) throws IOException {
        BufferedReader file = new BufferedReader(new FileReader("leap.in"));
        String line = file.readLine();
        int numberOfCases = Integer.parseInt(line);
        String result = "";

        for (int i = 0; i < numberOfCases; i++) {
            line = file.readLine();
            String[] arguments = line.split(" ");
            long year1 = Long.parseLong(arguments[0]);
            long year2 = Long.parseLong(arguments[1]);

            long check = isLeapYear(year1, year2, i);
            result += (i + 1);
            result += ". ";

            if (check == -1) {
                result += "Not a leap year!";
            } else {
                result += check;
            }
            result += "\n";
        }

        FileWriter write = new FileWriter("leap.answer");
        write.write(result);

        write.close();
        file.close();
    }

    public static long isLeapYear(long year1, long year2, int counter) {
        long temp = year2;
        while (!isLeapYear2(temp)) {
            temp--;
        }
        if (year1 % 100 != 0) {
            if (year1 % 4 == 0) {
                System.out.println(counter + ". year2: " +year2 + " temp: " + temp + " year1 " + year1 );
                return (temp - year1) / 4;
            } else {
                return -1;
            }
        } else if (year1 % 400 == 0) {
                System.out.println(counter + ". year2: " +year2 + " temp: " + temp + " year1 " + year1 );
            return (temp - year1) / 4;
        } else {
            return -1;
        }
    }

    public static boolean isLeapYear2(long year) {
        if (year % 100 != 0) {
            if (year % 4 == 0) {
                return true;
            } else {
                return false;
            }
        } else if (year % 400 == 0) {
            return true;
        } else {
            return false;
        }
    }
}