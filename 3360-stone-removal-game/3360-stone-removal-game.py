class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        n=n-10
        st=10
        while True:
            st=st-1
            if st>n:
                if st%2==0:
                    return False
                else:
                    return True
            n=n-st
