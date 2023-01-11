class Solution(object):
    def pivotIndex(self, nums):
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]


        if nums[-1] - nums[0] == 0:
            return 0
        else:
            for j in range(1, len(nums)):
                if nums[-1] - nums[j] == nums[j-1]:
                    return j
        return -1
        """
        :type nums: List[int]
        :rtype: int
        """
