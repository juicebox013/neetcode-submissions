class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add everything to hash set 
        numbers = set(nums)
        longest = 0

        for n in nums:
            #check if it is the start of a sequence
            if(n-1) not in numbers:
                #if it is the start, then we need to start counting how long this sequence is
                length = 0

                #this checks the current number we are at and adds 1 to the length every time we reach a 
                #number that is still in the set (there is no right neighbor)
                while (n + length) in numbers:
                    length += 1
                longest = max(length, longest)
        return longest

