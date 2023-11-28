import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.io.*;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("dance.in"));
        FileWriter file = new FileWriter(new File("dance.answer"));
        String result = "";
        int nOfCases = scan.nextInt();

        for (int i = 0; i < nOfCases; i++) {
            int numberOfDancers = scan.nextInt();
            int numberOfSensors = scan.nextInt();
            int K = scan.nextInt();
            ArrayList<int[]> dancers = new ArrayList<int[]>();
            ArrayList<int[]> sensors = new ArrayList<int[]>();

            for (int j = 0; j < numberOfDancers; j++) {
                int x = scan.nextInt();
                int y = scan.nextInt();
                int constantFactor = scan.nextInt();

                dancers.add(new int[] { x, y, constantFactor });
            }

            for (int j = 0; j < numberOfSensors; j++) {
                int x = scan.nextInt();
                int y = scan.nextInt();
                int rangeOfTheSensor = scan.nextInt();

                sensors.add(new int[] { x, y, rangeOfTheSensor });
            }

            int totalEnergy = 0;

            for(int[] dancer: dancers) {
                int nOfSensors = 0;
                for(int[] sensor: sensors) {
                    if(isIntersect(sensor, dancer)) {

                        nOfSensors++;
                    }
                }
                if (nOfSensors==0)
                    continue;
                totalEnergy += calculateEnergy(K, dancer[2], nOfSensors);
            }

            System.out.println(totalEnergy);
        }

        file.write(result);
        scan.close();
        file.close();
    }

    public static double calculateEnergy(int Kconstant, int energyExpected, int numberOfSensors) {
        return (Kconstant * energyExpected) / numberOfSensors;
    }

    public static boolean isIntersect(int[] sensor, int[] dancer) {
        if(calcDistance(dancer[0], dancer[1], sensor[0], sensor[1]) <= sensor[2]) {
            return true;
        } else {
            return false;
        }
    }

    public static double calcDistance(int x1, int y1, int x2, int y2) {
        return Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
    }

    public static void printArrayList(ArrayList<int[]> array) {
        for (int i = 0; i < array.size(); i++) {
            int[] arr = array.get(i);
            System.out.println(Arrays.toString(arr));
        }
    }
}