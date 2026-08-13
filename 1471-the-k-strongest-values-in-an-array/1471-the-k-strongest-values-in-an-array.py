class Solution:
    def getStrongest(self, a: List[int], k: int) -> List[int]:
        l=[]
        a.sort()
        m=a[(len(a)-1)//2]
        print(m)
        for i in a:
            l.append(abs(i-m))
        d={}
        freq={}
        for i in a:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        c=0
        for i in range(len(a)):
                d[a[i]]=l[i]
        d=dict(sorted(d.items(),key=lambda x:(-x[1],-x[0])))
        res=[]
        for i in d:
            while freq[i]>0:
                res.append(i)
                freq[i]-=1
        return res[:k]