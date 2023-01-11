class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        count = 1
        final = 0
        for _ in range(len(height)):
            a = min(height[i], height[j]) * (len(height) - count)
            if a > final:
                final = a
            count+=1
            if height[i] == height[j]:
                i+=1
            elif min(height[i], height[j]) == height[i]:
                i+=1
            elif min(height[i], height[j]) == height[j]:
                j-=1
            
        return final
        """
        :type height: List[int]
        :rtype: int
        """
