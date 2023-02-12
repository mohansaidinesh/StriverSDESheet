class Solution:
    def majorityElement(self, n: List[int]) -> int:
        d={}
        for i in n:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>len(n)//2:
                return i
    
