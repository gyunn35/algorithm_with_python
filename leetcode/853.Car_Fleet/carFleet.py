from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst = [(p, s) for p, s in zip(position, speed)]

        lst.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for item in lst:
            tmp = (target - item[0]) / item[1]
            if len(stack) == 0 or stack[-1] < tmp:
                stack.append(tmp)

        return len(stack)
