import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("crane.in"));
        FileWriter file = new FileWriter(new File("crane.answer"));
        String result = "";
        int testCases = scan.nextInt();

        for (int i = 0; i < testCases; i++) {
            int width = scan.nextInt();
            int height = scan.nextInt();
            int nOfCranes = scan.nextInt();
            int[] heightsOfCrane = new int[nOfCranes];
            int[][] matrix = new int[height][width];

            for (int a = 0; a < nOfCranes; a++) {
                heightsOfCrane[a] = scan.nextInt();
            }

            Arrays.sort(heightsOfCrane);

            for (int p = 0; p < heightsOfCrane.length / 2; p++) {
                int tempValue = heightsOfCrane[p];
                heightsOfCrane[p] = heightsOfCrane[heightsOfCrane.length - p - 1];
                heightsOfCrane[heightsOfCrane.length - p - 1] = tempValue;
            }

            System.out.println(Arrays.toString(heightsOfCrane));

            for (int a = 0; a < matrix.length; a++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    String num = scan.next();
                    if (num.equals("X")) {
                        matrix[a][j] = -1;
                    } else if (num.equals("0")) {
                        matrix[a][j] = 0;
                    } else {
                        matrix[a][j] = Integer.parseInt(num);
                    }
                }
            }

            int totalFloors = 0;

            for (int m = 0; m < heightsOfCrane.length; m++) {
                int[] bestPostion = calculate(heightsOfCrane[m], matrix);
                totalFloors += bestPostion[2];
            }

            result += (i + 1) + ". " + totalFloors;
            result += "\n";
        }
        System.out.println(result);

        file.write(result);
        scan.close();
        file.close();
    }

    public static int[] calculate(int crane, int[][] matrix) {
        int x = 0;
        int y = 0;
        int maxFloors = 0;
        ArrayList<int[]> bestNabourPositions = new ArrayList<int[]>();
        ;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    ArrayList<int[]> nabourPositions = getNabourPositions(i, j, matrix);
                    int floorsCalc = 0;

                    for (int b = 0; b < nabourPositions.size(); b++) {
                        int[] coordinate = nabourPositions.get(b);
                        // System.out.println(Arrays.toString(coordinate));
                        int currentPosition = matrix[coordinate[0]][coordinate[1]];
                        if (currentPosition != -1 && currentPosition != 0 && currentPosition < crane) {
                            floorsCalc += currentPosition;
                        }
                    }
                    // System.out.println(floorsCalc);

                    maxFloors = Math.max(maxFloors, floorsCalc);

                    if (maxFloors == floorsCalc) {
                        x = i;
                        y = j;
                        bestNabourPositions = nabourPositions;
                    }
                }
            }
        }

        for (int i = 0; i < bestNabourPositions.size(); i++) {
            int[] coordinate = bestNabourPositions.get(i);
            matrix[coordinate[0]][coordinate[1]] = -1;
        }

        return new int[] { x, y, maxFloors };
    }

    public static ArrayList<int[]> getNabourPositions(int x, int y, int[][] matrix) {
        ArrayList<int[]> result = new ArrayList<int[]>();
        result.add(new int[] { x - 1, y });
        result.add(new int[] { x + 1, y });

        result.add(new int[] { x, y - 1 });
        result.add(new int[] { x, y + 1 });

        result.add(new int[] { x - 1, y - 1 });
        result.add(new int[] { x + 1, y + 1 });

        result.add(new int[] { x + 1, y - 1 });
        result.add(new int[] { x - 1, y + 1 });

        for (int i = 0; i < result.size(); i++) {
            int[] coordinate = result.get(i);
            if (coordinate[0] >= matrix.length || coordinate[0] < 0 || coordinate[1] >= matrix[0].length
                    || coordinate[1] < 0) {
                result.remove(i);
                i--;
            }
        }

        return result;
    }

    public static void print2DArray(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static boolean sort(int a, int b) {
        return a < b;
    }
}

// 17 3 5
// [265, 172, 83, 52, 15] 
// 0   X   X   0   0   0   44  X   190 X   X   X   X   0   0   130 162 
// X   283 179 165 125 221 286 X   X   39  237 0   X   69  115 0   X   
// X   78  X   X   161 0   X   62  90  91  230 X   267 154 23  265 136 