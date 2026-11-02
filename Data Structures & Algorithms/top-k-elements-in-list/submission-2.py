class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use bucket sort. the bucket will have the number of times that is possible for a number to appear 
        #which is at most how many numbers in the list times.

        #then, the value will be a list containing which numbers appear that many times.
        #keep going until we reach k numbers in our result list.

        counts = {}
        frequencies = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for number, count in counts.items():
            frequencies[count].append(number)
        result = []
        for i in range(len(frequencies) - 1, 0 , -1):
            for number in frequencies[i]:
                result.append(number)
                if len(result) == k:
                    return result
