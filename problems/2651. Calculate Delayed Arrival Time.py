class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
    
        arrivalTime = arrivalTime + delayedTime

        if arrivalTime > 23:
            arrivalTime = arrivalTime % 24

        return arrivalTime


        