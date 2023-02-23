class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        l=[]
        for i in zip(*m):
            l.append(i[::-1])
        m[:]=l
