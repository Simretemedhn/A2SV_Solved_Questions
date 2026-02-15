#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        
        a_map = defaultdict(int)
        
        for num in a:
            a_map[num] += 1
        
        for nums in b:
            if a_map[nums] == 0:
                return False
            a_map[nums] -= 1
        return True 
        
        
        """for x in range(len(b)):
            if b[x] in a: 
                a.pop(a.index(b[x]))
            else:
                return False
        return True """
    
    
    
    
