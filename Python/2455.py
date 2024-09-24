class Solution(object):
    def averageValue(self, nums):
        sum =0
        count = 0
        for num in nums:
            if(num % 2 == 0 and num % 3 == 0):
                sum += num
                count += 1
        if count == 0:
            return 0
        else:
            return sum/count       
                
        """
        :type nums: List[int]
        :rtype: int
        """
        