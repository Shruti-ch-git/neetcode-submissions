class Solution:
    def isHappy(self, n: int) -> bool:

        def adds(num):
            total = 0

            while num > 0:
                digit = num % 10
                total += digit ** 2
                num //= 10

            return total

        store = set()

        while n != 1:
            if n in store:
                return False

            store.add(n)
            n = adds(n)

        return True