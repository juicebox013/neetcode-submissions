class Solution:

    def encode(self, strs: List[str]) -> str:
        #first we create an empty string
        result = ""
        
        #for each string in the list, we are adding the length of the string and the delimiter in front
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        #create an empty list since we are expected a list of string as a result
        result = []
        i = 0

        #while we are not at the end of the encoded string
        while i < len(s):
            #create a dummy pointer so we can pinpoint where the delimiter and length of string are
            j = i
            while s[j] != "#":
                j += 1
            #this is the integer value of how long the str is. we use j as the end of the substring since 
            #it is not included, so we only get the integer value of the length
            #dont forget to parse it back into an int
            length = int(s[i:j])

            #this adds the string without the length or delimiter back to the result list.
            result.append(s[j+1 : j+1+length])

            #now, we are updating the pointer i to the start of the next length/delimiter
            i = j+1+length
        return result
            
