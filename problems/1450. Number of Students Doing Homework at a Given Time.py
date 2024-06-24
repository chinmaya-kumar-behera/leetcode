class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for ind in range(len(startTime)):
            if startTime[ind] <= queryTime and queryTime <= endTime[ind]:
                count += 1
        return count