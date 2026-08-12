class Solution:
    def maxSubarrayLength(self, a: List[int], k: int) -> int:
        d={}
        st=0
        res=0
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=1
            else:
                d[a[i]]+=1
            if d[a[i]]>k:
                while a[st]!=a[i]:
                    d[a[st]]-=1
                    st+=1
                d[a[st]]-=1
                st+=1
            res=max(res,i-st+1)
        return res