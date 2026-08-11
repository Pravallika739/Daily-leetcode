class Solution:
    def frequencySort(self, a: List[int]) -> List[int]:
        d={}
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        d=dict(sorted(d.items(),key=lambda x:(x[1],-x[0])))
        res=[]
        for i in d:
            while d[i]>0:
                res.append(i)
                d[i]-=1
        return res