class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        st=0
        val=0
        res=0
        for i in range(len(gas)):
            val+=gas[i]-cost[i]
            res+=gas[i]-cost[i]
            if val<0:
                val=0
                st=i+1
        if res>=0:
            return st
        return -1