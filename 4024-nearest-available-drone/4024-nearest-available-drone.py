class Solution:
    def nearestDrone(self, a: list[list[int]], t: list[int]) -> int:
        mini=float('inf')
        ind=-1
        for i in range(len(a)):
            val=abs(a[i][0]-t[0])+abs(a[i][1]-t[1])
            if val<=a[i][2] and val<mini:
                mini=val
                ind=i
        return ind
                