class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals is None or len(intervals) == 0:
            return []
        def sortFirst(val):
            return val[0]
        intervals.sort(key=sortFirst)
        start = intervals[0][0]
        end = intervals[0][1]
        result = []
        for i in range(1, len(intervals)):
            if end >= intervals[i][0] and start <= intervals[i][1]:
                end = intervals[i][1] if end <= intervals[i][1] else end
                start= intervals[i][0] if start >= intervals[i][0] else start
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start, end])
        return result
        