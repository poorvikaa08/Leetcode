class Solution(object):
    def isThree(self, n):
        if n==1 and n==2:
            return False
        count = 1
        for i in range(2,n+1):
            if n%i == 0:
                count += 1
            if (count>3):
                return False
        if count == 3:
            return True
        
        
  #    return sum(n%i == 0 for i in range(1, n+1)) == 3)
  
        """
        :type n: int
        :rtype: bool
        """
        