class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #it is nondecreasing so that means there can be numbers that are the same
        #need to use two pointers to solve this problem
        #if the target is lower, then move the right pointer back one. 
        #if the target is higher, then move the left pointer over one.
        i = 0
        j = len(numbers) - 1 
        while i < j:
            n = numbers[i] + numbers[j]
            #if it is lower than target, move left pointer up
            if n < target:
                i += 1
            elif n > target:
                j -= 1
            elif n == target:
                # need to add one because we are using 1-indexing
                return [i + 1, j + 1]