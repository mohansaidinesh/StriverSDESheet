class Solution:
    def findDuplicate(self, l: List[int]) -> int:
        d={}
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]>=2:
                return i
