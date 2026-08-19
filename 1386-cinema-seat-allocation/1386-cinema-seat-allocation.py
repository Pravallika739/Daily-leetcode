class Solution:
    def maxNumberOfFamilies(self, n: int, a: List[List[int]]) -> int:
        res=0
        a.sort()
        i=0
        val=0
        while i<len(a):
            fi=0
            se=0
            th=0
            c=a[i][0]
            while i<len(a) and a[i][0]==c:
                e=a[i][1]
                if e==2 or e==3 or e==4 or e==5:
                    fi=1
                if e==6 or e==7 or e==8 or e==9:
                    se=1
                if e==4 or e==5 or e==6 or e==7:
                    th=1
                i+=1
            if fi==1 or se==1 or th==1:
                res=res+min(1,(3-fi-se-th))
            else:
                res=res+2
            val+=1
        res+=((n-val)*2)
        return res