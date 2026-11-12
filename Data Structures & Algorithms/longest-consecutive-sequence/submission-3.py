class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        nums = set(nums)
        for n in nums:
            if (n-1) not in nums:
                current = 0
                while (n+current) in nums:
                    current += 1
                result = max(current, result)
        return result
