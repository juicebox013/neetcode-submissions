class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            word = {}
            for char in string:
                word[char] = word.get(char, 0) + 1
            #we need to convert the hashmap into tuple because python dictionaries cannot
            #be used as keys in another dictionary 
            #we also need to sort them since we turned it into a tuple and need to check equivalency
            key = tuple(sorted(word.items()))
            if key not in groups:
                #creating an empty list so we can add the words later
                groups[key] = []
            groups[key].append(string)
        return list(groups.values())


        
        