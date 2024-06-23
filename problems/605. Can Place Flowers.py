class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        ind = 0

        while ind < len(flowerbed):
            if flowerbed[ind] == 1:
                ind += 2
            else:
                if len(flowerbed)-1 == ind or flowerbed[ind+1] == 0:
                    n -= 1
                    flowerbed[ind] = 1
                    ind += 2
                else:
                    ind += 1
            
            if n <= 0:
                return True              
               
        return n <= 0  
       

print(Solution().canPlaceFlowers([0,1,0],1))
        