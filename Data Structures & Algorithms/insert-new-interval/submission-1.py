class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''sorted, start and end is given 
        insert= sorted, merge if overlapped'''
        res=[]
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] # new end is smaller than start of next
            elif newInterval[0]> intervals[i][1]: 
                res.append(intervals[i]) # new start is greater than the end of next
            else:
                mini= min(newInterval[0], intervals[i][0])
                maxi= max(newInterval[1], intervals[i][1])
                newInterval=[mini, maxi]
        res.append(newInterval)
        return res

        