class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[j] == 0:
                j -= 1
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0) 
                j-=1
            else:
                i+=1
        return nums


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
