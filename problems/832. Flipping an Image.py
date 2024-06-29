class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        for i in range(len(image)):
            image[i] = [ 1 if n==0 else 0 for n in image[i][::-1] ]
        
        return image




print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))