class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        start.sort()
        end.sort()
        result = 0
        endItr = 0
        for i in range(len(start)):
            if start[i] < end[endItr]:
                result += 1
            else:
                endItr += 1
        return result