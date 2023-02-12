class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, a):
        d = {}
        res=[]
        max = len(a)
        for i in a:
            if not i in d:
                d[i] = True   
            else:
                res.append(i)
        for i in range(1, max + 1):
            if not i in d:
                res.append(i)
        return res
            
