class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the length of piles <= h 
        # the largest value of k that we can find is the value of the highest pile. this is our UPPER BOUND
        # we can initialize an array that is [1:piles[-1]] (sorted piles) and use binary search on that array and test it as a k value.
        #if that middle value does not work, it is too low, so we remove all those values and move the left pointer to middle + 1.
        #if that middle value does work, it could potentially be too high, so lets try removing all the values on the right (middle - 1) and continue.
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            k = (right + left) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1
        return result
            
