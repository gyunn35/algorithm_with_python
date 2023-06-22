from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 0
        left, right = 0, len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[res]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return nums[res]
