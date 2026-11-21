class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        #this portion checks if the array is ALREADY sorted in ascending order.
        while l <= r:
            #if the leftmost value is smaller than the rightmost, the minimum is the left, break out of loop
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            #if the array is NOT in ascending order, we need to check the right/left portions of array from midpoint
            m = (l + r) // 2
            res = min(res, nums[m])
            #if the middle is greater than or equal to the left pointer, we know that the minimum value must in the right portion of the array since we already confirmed it is not in asceidnign order. 
            if nums[m] >= nums[l]:
                l = m + 1
            #if the middle is smaller than the left pointer, we know it is in the left portion of the array. 
            else:
                r = m - 1
        return res