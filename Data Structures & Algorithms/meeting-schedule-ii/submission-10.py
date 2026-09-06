"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #two pointer method = time exceeded
        # priority queue method needed

        #sort start times
        start_times = sorted(i.start for i in intervals)
        #sort end times
        end_times = sorted(i.end for i in intervals)
        # two pointer
        i, j = 0, 0
        # rooms for max of rooms at a certain point 
        # result for max number of rooms that was needed throughout iteration -> will return this 
        rooms, result = 0, 0
        while i < len(start_times): #do not need a while loop to make sure j is < len(end_times) because start times will always end first
            if start_times[i] < end_times[j]:
                rooms += 1
                i += 1
            else:
                j += 1
                rooms -= 1
            result = max(result, rooms)
        return result

            
                    

       





        