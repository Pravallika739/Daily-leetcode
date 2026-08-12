class Solution:
    def countFairPairs(self, a: List[int], l: int, h: int) -> int:
        i=0
        end=len(a)-1
        a.sort()
        cnt=0
        while i<end:
            if a[i]+a[end]<=h:
                cnt+=(end-i)
                i+=1
            else:
                end-=1
        i=0
        end=len(a)-1
        while i<end:
          if a[i]+a[end]<l:
            cnt-=(end-i)
            i+=1
          else:
            end-=1
        return cnt