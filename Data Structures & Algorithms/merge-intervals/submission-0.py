class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_val = result[-1][1]
            if start <= last_val:
                result[-1][1] = max(last_val, end)
            else:
                result.append([start,end])
        return result