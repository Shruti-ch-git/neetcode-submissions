class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sym = ["+", "-", "/", "*"]
        for c in tokens:
            if c not in sym:  # If it's not an operator, push it onto the stack as an integer
                stack.append(int(c))  # Change made here: Convert string to integer
            else:
                b = stack.pop()  # Pop the second operand first (right side of the operator)
                a = stack.pop()  # Pop the first operand (left side of the operator)
                
                if c == "+":
                    sol = a + b
                elif c == "-":
                    sol = a - b
                elif c == "*":
                    sol = a * b
                elif c == "/":
                    sol = int(a / b)  # Change made here: Use integer division that truncates toward zero
                
                stack.append(sol)  # Push the result back onto the stack
        
        return stack[-1]  # Return the final result after all tokens have been processed (change made here)
