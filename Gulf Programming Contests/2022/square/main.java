import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import java.io.*;

public class main {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new File("square.in"));
        FileWriter file = new FileWriter(new File("biplay.answer"));
        int line = scan.nextInt();
        String result = "";
        int cases = 1;

        while (line != 0) {
            int matrixDimentions = line;
            int[][] horizental = new int[matrixDimentions][matrixDimentions - 1];
            int[][] vertical = new int[matrixDimentions - 1][matrixDimentions];

            // Fill up horizental array
            for (int i = 0; i < horizental.length; i++) {
                for (int j = 0; j < horizental[0].length; j++) {
                    horizental[i][j] = scan.nextInt();
                }
            }

            // Fill up vertical array
            for (int i = 0; i < vertical.length; i++) {
                for (int j = 0; j < vertical[0].length; j++) {
                    vertical[i][j] = scan.nextInt();
                }
            }

            int largestSquarePossible = matrixDimentions - 1;

            int[] scoreMap = new int[largestSquarePossible + 1];

            print2DArray(horizental);
            print2DArray(vertical);

            // Calculate each
            for (int i = 0; i < vertical.length; i++) {
                for (int j = 0; j < horizental.length; j++) {
                    for (int n = 1; n <= largestSquarePossible; n++) {
                        if (i + n >= matrixDimentions || j + n >= matrixDimentions) {
                            continue;
                        }
                        boolean isSquare = true;
                        for (int a = 0; a < n; a++) {
                            if (horizental[i][j] == 0 || horizental[i][j + a] == 0
                                    || horizental[i + n][j] == 0 || horizental[i + n][j + a] == 0) {
                                isSquare = false;
                            }

                            if (vertical[i][j] == 0 || vertical[i + a][j] == 0
                                    || vertical[i][j + n] == 0 || vertical[i + a][j + n] == 0) {
                                isSquare = false;
                            }
                        }

                        if (isSquare) {
                            scoreMap[n]++;
                        }
                    }
                }
            }

            int counter = 0;
            result += "Case " + cases + "\n";
            for (int score : scoreMap) {
                if (score != 0) {
                    result += counter + ": " + score;
                    result += "\n";
                }
                counter++;
            }

            line = scan.nextInt();
            cases += 2;
            result+="\n";
        }

        file.write(result);
        file.close();
        scan.close();
    }

    public static int[][] constructMatrix(int[][] horizental, int[][] vertical) {
        int[][] matrix = new int[horizental.length][vertical.length];

        return matrix;
    }

    public static void print2DArray(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
