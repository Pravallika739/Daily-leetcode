class Solution:
    def longestConsecutive(self, l: List[int]) -> int:
        l=list(set(l))
        l.sort()
        res=0
        i=0
        while i<len(l):
            c=1
            while i<len(l) and l[i]==l[i-1]+1:
                i+=1
                c+=1
            res=max(res,c)
            i+=1
        return res