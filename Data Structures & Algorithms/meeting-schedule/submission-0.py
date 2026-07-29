"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by their start time directly
        intervals.sort(key=lambda x: x.start)
        
        for i in range(len(intervals) - 1):
            # If current meeting ends AFTER the next meeting starts -> conflict!
            if intervals[i].end > intervals[i + 1].start:
                return False
                
        return True
            
