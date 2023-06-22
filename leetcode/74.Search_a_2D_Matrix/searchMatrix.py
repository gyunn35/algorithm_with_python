from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        while left <= right:
            row = (left + right) // 2
            if matrix[row][0] > target:
                right = row - 1
            elif matrix[row][-1] < target:
                left = row + 1
            else:
                break

        if left > right:
            return False

        row = (left + right) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2  # prevent overflow
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
