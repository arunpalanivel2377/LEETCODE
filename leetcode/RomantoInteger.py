class Solution:
    def romanToInt(self, s: str) -> int:
        self.dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        result = 0
        i = 0
        while i < len(s):

            if i+1 < len(s) and self.dict1[s[i]] < self.dict1[s[i+1]]:
                result += self.dict1[s[i+1]] - self.dict1[s[i]]

                i += 1
            else:
                result += self.dict1[s[i]]
            i += 1
        return result
    

