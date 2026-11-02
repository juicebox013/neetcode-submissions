class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str_s = {}
        str_t = {}
        for i in range(len(s)):
            str_s[s[i]] = 1 + str_s.get(s[i], 0)
            str_t[t[i]] = 1 + str_t.get(t[i], 0)
        return str_s == str_t
            
        
        