class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []

        for i in range(len(s)):
            if s[i] == "(":
                openStack.append(i)

            elif s[i] == "*":
                starStack.append(i)

            else:  # s[i] == ")"
                if openStack:
                    openStack.pop()

                elif starStack:
                    # Use an earlier * as "("
                    starStack.pop()

                else:
                    # Nothing can match this ")"
                    return False

        # Use remaining stars as closing ")"
        while openStack and starStack:
            # The star must occur after the opening parenthesis
            if openStack[-1] > starStack[-1]:
                return False

            openStack.pop()
            starStack.pop()

        return len(openStack) == 0