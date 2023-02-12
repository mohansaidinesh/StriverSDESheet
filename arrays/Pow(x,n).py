class Solution:
    def myPow(self, x: float, n: int) -> float:
        def trav(x,n):
            if n==0:
                return 1
            if n%2==0:
                return trav(x*x,n//2)
            else:
                return x*trav(x*x,(n-1)//2)
        t=trav(x,abs(n))
        return t if n>=0 else 1/t
