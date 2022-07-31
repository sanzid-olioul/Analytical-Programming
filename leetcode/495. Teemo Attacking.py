class Solution:
   def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    
    result  = []
    dur = 0
    end= 0
    for i in range(0,len(timeSeries)):
        if timeSeries[i] <= end :
            dur = dur + timeSeries[i] + duration - end
            end = timeSeries[i] + duration
        else:
            dur = dur + duration 
            end = timeSeries[i] + duration
    return dur