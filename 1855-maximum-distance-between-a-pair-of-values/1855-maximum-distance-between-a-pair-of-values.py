class Solution:
    def maxDistance(self, a: List[int], b: List[int]) -> int:
        i,j=min(len(b)-1,len(a)-1),len(b)-1
        res=-1
        c=0
        while i>=0 and j>=0 and j>=i:
            if b[j]>=a[i]:
                res=max(res,abs(j-i))
                i-=1
            else:
                if i>=j:
                    i-=1
                j-=1
        if res==-1:
            return 0
        return res