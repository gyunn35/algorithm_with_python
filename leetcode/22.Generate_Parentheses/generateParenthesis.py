from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(open_cnt, close_cnt):
            if open_cnt == close_cnt == n:
                res.append("".join(stack))
                return

            if open_cnt < n:
                stack.append("(")
                dfs(open_cnt + 1, close_cnt)
                stack.pop()
            if close_cnt < open_cnt:  # close_cnt must be less than open_cnt
                stack.append(")")
                dfs(open_cnt, close_cnt + 1)
                stack.pop()

        dfs(0, 0)

        return res
