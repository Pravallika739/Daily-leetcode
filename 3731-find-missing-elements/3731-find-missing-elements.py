class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        c=nums[0]
        l=[]
        i=0
        while(len(nums)>i):
            if c!=nums[i]:
                l.append(c)
            else:
                i+=1
            c+=1
        return l