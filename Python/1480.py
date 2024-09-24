class Solution(object):
    def runningSum(self, nums):
        sum = 0
        output = []
        for num in nums:
            sum += num
            output.append(sum)

        return output  
        
           
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        