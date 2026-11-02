class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #the product of every numer to the left of the current index is the prefix
        #the product o every number to the right of the current index is the postfix
        #the first element has a defeault prefix of 1
        #the last element has a default postfix of 1
        #by multiplying the postfix/prefix, we dont include the value at current index in product


        #we are first creating the result list with default values of 1 so we can multiply correctly later
        res = [1] * (len(nums))

        #the prefix will start at 1 for the initial index
        prefix = 1

        #here, we are going through each position of the input array
        for i in range(len(nums)):
            #first, we are putting the prefix values into the result array, so we can multiply it by
            #the postfix later
            res[i] = prefix

            #here, we are updating the prefix to include the current number we are on, before moving to the
            #next number in the list
            prefix *= nums[i]

        #here, we are doing the same process, but going from right to left in the input array for postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
        