class Solution:
    def maxProfit(self, a: List[int]) -> int:
        maxi=0
        res=0
        req=a[0]
        for i in range(1,len(a)):
            if a[i]<a[i-1]:
                res+=maxi
                maxi=0
                req=a[i]
            else:
                maxi=max(maxi,a[i]-req)
        res+=maxi
        return res