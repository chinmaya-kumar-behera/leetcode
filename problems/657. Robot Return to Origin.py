class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        m = {"R":('x',1), "L":('x',-1),"U":('y',1),"D":('y',-1)}
        cord = {'x':0,'y':0}

        for step in moves:
            dir,val = m[step]
            cord[dir] += val
        
        return tuple(cord.values()) == (0,0)
    
        #  ANOTHER APPROACH

        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
    



print(Solution().judgeCircle("UD")) 
