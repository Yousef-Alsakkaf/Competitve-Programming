import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class main {
    public static int minr(int n, List<int[]> mp, int m) {

        int[][] dp = new int[n][n];
        int count = 0;
        int i = 0, j = 0;

        // To mark the cells having mines by -1
        for (int[] x : mp) {
            dp[x[0]][x[1]] = -1;
        }

        int numberOfRobots = 0;

        while (count != m) {
            numberOfRobots++;
            // checking if i reached end of grid
            i = 0;
            j = 0;
            while (i < n - 1 || j < n - 1) {
                boolean hasmoved = false;
                int row = i;
                int col = j;

                if (dp[row][col] == -1) {
                    dp[row][col] = 0;
                    count++;
                }

                // while loop to move to the down
                while (row < n && dp[i][j] != -1) {
                    if (dp[row][col] == -1) {
                        i += row - i;
                        // System.out.println("-1 spotted down side" + " i= " + i + " j=" + j);
                        hasmoved = true;
                        dp[row][col] = 0;
                        count++;
                        break;
                    }
                    row++;
                }
                row = i;

                while (col < n && dp[i][j] != -1 && !hasmoved) {
                    if (dp[row][col] == -1) {
                        j += col - j;
                        //System.out.println("-1 spotted right side " + " i= " + i + " j=" + j);
                        hasmoved = true;
                        dp[row][col] = 0;
                        count++;
                        break;
                    }
                    col++;
                }

                if (!hasmoved) {
                    if (i < n - 1) {
                        i++;
                    }

                    if (j < n - 1) {
                        j++;
                    }
                }
            }
        }
        return numberOfRobots;
    }

    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        Scanner scan = new Scanner(new File("robots.in"));
        int k = scan.nextInt(); // number of test cases
        int n = scan.nextInt(); // size of mines
        String result = "";

        for (int q = 0; q < k ; q++) {
            int m = scan.nextInt(); // number of mines
            List<int[]> mp = new ArrayList<>();

            for (int i = 0; i < m; i++) {
                int p = scan.nextInt();
                mp.add(new int[] { p / n, p % n });

            }

            result += "Case " + (q + 1) + ": " + minr(n, mp, m);
            result += "\n";
        }


        FileWriter file = new FileWriter("robots.answer");
        file.write(result);

        file.close();
        scan.close();
    }
}