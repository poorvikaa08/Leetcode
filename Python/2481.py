class Solution(object):
    def numberOfCuts(self, n):
        if n==1:
            return 0
        ans = (n/2,n)(n%2==0)
        return ans
        """
        :type n: int
        :rtype: int
        """
        