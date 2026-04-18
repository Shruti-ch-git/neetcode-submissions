class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)  # Initialize the result array with all 0s
        stack = []  # Stack to store pairs of (temperature, index)

        # Iterate through the temperatures array
        for i, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the stack's top temperature
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  # Pop the top element from the stack
                res[stackInd] = i - stackInd  # Calculate the difference in days and store it in the result array
            
            # Push the current temperature and its index onto the stack
            stack.append((t, i))
        
        return res  # Return the final result
