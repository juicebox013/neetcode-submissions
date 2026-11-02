class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #need to first turn all the words into different hashmaps. 
        #then check if the values for that hashmap is in the group hashmap. if not, add an empty list
        #then add that word to the respective group hashmap value
        #then return the hashmap.values()
        groups = {}
        for word in strs:
            word_freq = {}
            for i in range(len(word)):
                word_freq[word[i]] = 1 + word_freq.get(word[i], 0)
            key = tuple(sorted(word_freq.items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())


        
        