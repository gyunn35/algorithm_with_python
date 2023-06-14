import math
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = float("-inf")

        while i < j:
            area = (j - i) * min(height[i], height[j])
            res = max(res, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res


def main():
    tests = [
        (1, [1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        (2, [1, 1], 1),
    ]

    sol = Solution()

    for test in tests:
        actual = sol.maxArea(test[1])
        if actual != test[2]:
            print(f"{test[0]}: expected {test[2]}, but actual {actual}")


main()
