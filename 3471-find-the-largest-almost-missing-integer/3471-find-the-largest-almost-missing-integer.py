class Solution:
    def largestInteger(self, l: List[int], k: int) -> int:
        d={}
        for i in l:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        m=-1
        if k==1:
            for i in d:
                if d[i]==1:
                    m=max(m,i)
        elif k==len(l):
            for i in d:
                m=max(m,i)
        else:
            if d[l[0]]==1:
                m=max(m,l[0])
            if d[l[-1]]==1:
                m=max(m,l[-1])
        return m