class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Convert negative exponent:
        # x^(-n) = (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        while n > 0:
            # If n is odd, include the current x
            if n % 2 == 1:
                result *= x

            # Square the base and halve the exponent
            x *= x
            n //= 2

        return result