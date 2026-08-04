class Solution:
    def maximumUniqueSubarray(self, a: List[int]) -> int:
        h=set()
        l=0
        s=0
        res=0
        for i in range(len(a)):
            if a[i] not in h:
                s+=a[i]
            else:
                while a[i] in h:
                    h.remove(a[l])
                    s-=a[l]
                    l+=1
                s+=a[i]
            res=max(res,s)
            h.add(a[i])
        return res
