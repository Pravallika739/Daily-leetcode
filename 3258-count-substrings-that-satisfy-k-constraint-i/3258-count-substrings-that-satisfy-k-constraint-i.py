class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res=0
        for i in range(len(s)):
            zeroes=0
            ones=0
            for j in range(i,len(s)):
                if s[j]=='0':
                   zeroes+=1
                else:
                   ones+=1
                if zeroes>k and ones>k:
                    break
                res+=1
        return res