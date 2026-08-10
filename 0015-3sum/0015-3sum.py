class Solution:
    def threeSum(self, a: list[int]) -> list[list[int]]:
        a.sort()
        n=len(a)
        res=[]
        i=0
        while i<n-2:
            if i>0:
               while i<n and a[i]==a[i-1]:
                i+=1
            st=i+1
            end=n-1
            while end>st:
                val=a[st]+a[end]
                if val==-a[i]:
                    res.append([a[i],a[st],a[end]])
                    st1=st+1
                    end1=end-1
                    while st1<n and  a[st1]==a[st]:
                        st1+=1
                    while end1>=0 and a[end1]==a[end]:
                        end1-=1
                    st=st1
                    end=end1
                elif val<-a[i]:
                    st+=1
                else:
                    end-=1
            i+=1
        return res