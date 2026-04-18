class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed, then sort by position in reverse order (from farthest to closest)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []  # Stack to keep track of the times to reach the target for each fleet

        for p, s in pair:
            # Calculate the time it takes for the current car to reach the target
            t = (target - p) / s
            # If the stack is not empty and the car's time is less than or equal to the last fleet's time
            if stack and stack[-1] >= t:
                continue  # This car joins the previous fleet, no need to add a new fleet
            # Otherwise, push the time of this car to the stack as it forms a new fleet
            stack.append(t)

        return len(stack)  # The number of fleets is the size of the stack
