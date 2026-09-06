"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort first so then you only need to compare a meeting room to the one before it
        # list.sort(): modifies the list in place BUT new_list = sorted(list) returns a new sorted list
        # Both have two optional arguments: key (what to sort by), reverse (what direction to sort)
        # anonymous functions (lambda) syntax -> argument: return value
        intervals.sort(key = lambda x: x.start)
        # now intervals is sorted
        for i in range(1, len(intervals)): # start at 1 so can compare with prev intervals
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True

                
                
            
            



