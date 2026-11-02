class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = str(len(s))
            encoded += length + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        length = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j+1+length
        return result

            
        
            
