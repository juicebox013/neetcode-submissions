class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #position = [1,4]
        #speed = [3,2]
        #zip(position, speed) --> [(1,3), (4,2)]
        pair = [(position, speed) for position, speed in zip(position, speed)]
        #this sorts the array in descending order
        pair.sort(reverse=True)
        stack = []
        for position, speed in pair:  # Reverse Sorted Order
            #this calculates in what time the current car will reach the goal
            stack.append((target - position) / speed)
            #if there are atleast 2 cars to compare AND
            #the current car is faster than the one in front of it, it will be limited by that car with the slower speed and become a fleet. pop it off because it doesnt matter
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        #the amount of speeds in the final stack are how many fleets there are.
        return len(stack)