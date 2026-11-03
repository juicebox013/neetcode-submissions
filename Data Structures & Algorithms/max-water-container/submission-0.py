class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we should use two pointers
        #the only way for it to be worth to move our pointers inward would be if the walls get taller.
        #keep a most counter and a current counter. return the max(current, most) at the end.
        right = len(heights) - 1
        left = 0
        most = 0
        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            most = max(current, most)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return most

                     
