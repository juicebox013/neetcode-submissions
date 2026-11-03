class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, number in enumerate(nums):
            if number > 0:
                break

            if index > 0 and number == nums[index - 1]:
                continue
            
            left = index + 1
            right = len(nums) -1
            while left < right:
                three_sum = number + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    result.append([number, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result

