class Solution:
    def maximumLengthSubstring(self, a: str) -> int:
        d={}
        st=0
        res=0
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=1
            else:
                d[a[i]]+=1
            while d[a[i]]>2:
                d[a[st]]-=1
                st+=1
            res=max(res,i-st+1)
        return res