#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size(), column = matrix[0].size();
        int topRow = 0, bottomRow = rows - 1;

        while (topRow <= bottomRow) {
            int row = (topRow + bottomRow) / 2;
            if (matrix[row][column - 1] < target) {
                topRow = row + 1;
            } else if (matrix[row][0] > target) {
                bottomRow = row - 1;
            } else {
                break;
            }
        }

        if (topRow > bottomRow) {
            return false;
        }

        int row = (topRow + bottomRow) / 2;
        int left = 0, right = column - 1;

        while (left <= right) {
            int middle = (left + right) / 2;
            if (matrix[row][middle] == target) {
                return true;
            } else if (matrix[row][middle] < target) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        return false;
    }
};
