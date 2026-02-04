class Solution:    
    def findUnion(self, a, b):
        # code here
        uni = []
        visited = set()
        for x in a:
            if x not in visited:
                visited.add(x)
                uni.append(x)
        for y in b:
            if y not in visited:
                visited.add(y)
                uni.append(y)

        return uni 
        
   
