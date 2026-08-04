class Solution:
    def maxDistance(self, a: List[int], b: List[int]) -> int:
       res=float('-inf')
       n=len(a)
       m=len(b)
       i,j=0,0
       while i<n and j<m:
         if i<=j and a[i]<=b[j]:
            res=max(res,j-i)
            j+=1
         else:
            i+=1
            j+=1
       if res==float('-inf'):
        return 0
       return res