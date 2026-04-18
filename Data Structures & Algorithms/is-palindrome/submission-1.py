class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l < r:
            while l<r and not s[l].isalnum(): #only letters and/or digits and is not empty
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True





"""      
sentence = " This is a sentence with spaces. "
sentence = sentence.replace(" ", "")
print(sentence) 
# Output: "Thisisasentencewithspaces."
import re

original_sentence = "H!e(l)l*o, W@o#r$l%d! 123"

# Keep only letters (a-z, A-Z) and replace all other characters with an empty string
cleaned_sentence = re.sub(r'[^a-zA-Z]', '', original_sentence)

print(f"Original: {original_sentence}")
print(f"Cleaned:  {cleaned_sentence}")
"""
