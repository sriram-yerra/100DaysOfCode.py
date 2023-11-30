# intervals = [[1,3],[15,18],[2,6],[8,10]]
# intervals.sort()
# print(intervals)

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


