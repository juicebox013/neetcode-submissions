class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #creating a hashmap to first get how many times each number appears
        count = {}
        #creating a list of empty lists. we use len(nums) bc the most times a num can appear is the length
        # of nums
        freq = [[] for i in range(len(nums) + 1)]

        #updating the hashmap counts for each num in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #n is the number, c is how many times it appears. items() gives key-value pairs
        for n, c in count.items():
            #for each count, we are adding that number into the respective box
            freq[c].append(n)
        result = []

        #this line is iterating backwards through freq. in python, the syntax is range(start, stop, step)
        #we iterate backwards so we can return which ones appear the MOST first.
        for i in range(len(freq) - 1, 0, -1):
            #iterate through each bucket of counts
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result