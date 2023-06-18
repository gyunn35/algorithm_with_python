from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while len(stack) != 0 and temperatures[stack[-1]] < v:
                t = stack.pop()
                res[t] = i - t

            stack.append(i)

        return res
