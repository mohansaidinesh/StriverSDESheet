class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(0,n):
            for j in range(i,n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(0,n):
            for j in range(0,n//2):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][n-1-j]
                matrix[i][n-j-1]=temp
                
                
                
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        l=[]
        for i in zip(*m):
            l.append(i[::-1])
        m[:]=l
