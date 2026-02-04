class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a = sorted(a)
        b = sorted(b)
        for x in range(len(a)):
            if a[x] != b[x]:
                return False 
        return True 
