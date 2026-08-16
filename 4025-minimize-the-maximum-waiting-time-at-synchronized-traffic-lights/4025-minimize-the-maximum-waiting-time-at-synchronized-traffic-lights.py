class Solution:
    def minPenalty(self, p: int, l: list[int], a: list[int]) -> int:
        m=max(l)
        maxi=float('-inf')
        for i in range(len(a)):
            r=a[i]%p
            if r>=m:
                maxi=max(maxi,p-r)
        if maxi==float('-inf'):
            maxi=0
        return maxi
            