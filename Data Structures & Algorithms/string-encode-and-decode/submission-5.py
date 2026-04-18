class Solution:
    def encode(self, strs: list[str]) -> str:
        # Manually encode each string with its length followed by the separator and the string itself
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s  # Length of the string + separator + the string
        return encoded

    def decode(self, encoded: str) -> list[str]:
        # Manually decode the string by reading the number (length) until the separator
        strs = []
        i = 0
        
        while i < len(encoded):
            # Find the position of the separator '#'
            j = i
            while encoded[j] != '#':
                j += 1
            
            # The number represents the length of the string
            length = int(encoded[i:j])
            
            # The string starts after the '#' and has the specified length
            strs.append(encoded[j + 1: j + 1 + length])
            
            # Move the index `i` to the position after the current string
            i = j + 1 + length
        
        return strs
