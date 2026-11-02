class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_s = {}
        list_t = {}
        for i in range(len(s)):
            list_s[s[i]] = list_s.get(s[i], 0) + 1
            list_t[t[i]] = list_t.get(t[i], 0) + 1    
        return list_s == list_t
            
        
        