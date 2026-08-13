class Solution:
    def longestSubarray(self, l: List[int]) -> int:
        left=0
        res=0
        zeroes=0
        for i in range(len(l)):
            if l[i]==0:
                zeroes+=1
            if zeroes>1:
                while l[left]!=0:
                    left+=1
                left+=1
                zeroes=1
            res=max(res,(i-left+1-zeroes))
        if res==len(l):
            res-=1
        return res