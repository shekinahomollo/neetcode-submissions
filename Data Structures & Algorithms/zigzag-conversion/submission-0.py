class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = []
        n = len(s)
        cycleLen = 2 * numRows - 2

        for row in range(numRows):
            for j in range(row, n, cycleLen):
                # Character on the downward leg
                result.append(s[j])
                # Character on the upward leg (middle rows only)
                if row > 0 and row < numRows - 1:
                    second = j + cycleLen - 2 * row
                    if second < n:
                        result.append(s[second])

        return ''.join(result)