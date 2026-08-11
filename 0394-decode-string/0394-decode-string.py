class Solution:
    def decodeString(self, a: str) -> str:
        s1=[]
        s2=[]
        i=0
        st=""
        while i<len(a):
            if a[i]>='a':
                while i<len(a) and a[i].isalpha():
                    st+=a[i]
                    i+=1
            elif a[i].isdigit():
                n=0
                while a[i].isdigit():
                    n=(n*10)+int(a[i])
                    i+=1
                s2.append(n)
            elif a[i]=='[':
                s1.append(st)
                st=""
                i+=1
            else:
                a1=s1.pop()
                a2=s2.pop()
                st=a1+(st*a2)
                i+=1
        return st