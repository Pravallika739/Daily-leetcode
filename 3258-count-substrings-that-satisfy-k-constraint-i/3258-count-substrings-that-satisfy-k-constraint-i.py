class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res=0
        zeroes=0
        ones=0
        i=0
        l=0
        while i<len(s):
            if s[i]=='0':
                zeroes+=1
            else:
                ones+=1
            if zeroes>k and ones>k:
                while zeroes>k and ones>k:
                    if s[l]=='0':
                        zeroes-=1
                    else:
                        ones-=1
                    l+=1
            res+=(i-l+1)
            i+=1
        return res