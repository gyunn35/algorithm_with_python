from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        res = 0
        while left < right:
            if left_max < right_max:
                left += 1
                res += max(0, min(left_max, right_max) - height[left])
                left_max = max(left_max, height[left])
            else:
                right -= 1
                res += max(0, min(left_max, right_max) - height[right])
                right_max = max(right_max, height[right])

        return res


def main():
    tests = [
        (1, [4, 2, 0, 3, 2, 5], 9),
        (2, [0, 0, 0, 2, 4], 0),
        (3, [0, 0, 0, 5], 0),
        (4, [0, 0, 4, 2, 0], 0),
        (5, [0, 0, 0], 0),
        (6, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ]

    sol = Solution()

    for test in tests:
        actual = sol.trap(test[1])
        if test[2] != actual:
            print(f"{test[0]}: expected {test[2]}, but actual {actual}")


main()
