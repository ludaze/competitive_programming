class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def values(expr):
            ans, number = [], 0
            for i in range(len(expr)):
                if not expr[i].isdigit():
                    for left in values(expr[:i]):
                        for right in values(expr[i+1:]):
                            if expr[i] == '+': ans.append(left + right)
                            elif expr[i] == '-': ans.append(left - right)
                            elif expr[i] == '*': ans.append(left * right)
                else: number = number * 10 + int(expr[i])
            return ans if ans else [number]
        return values(expression)