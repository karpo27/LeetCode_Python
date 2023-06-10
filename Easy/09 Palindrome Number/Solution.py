class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        reversed_text = ""
        for letter in reversed(text):
            reversed_text += letter
            
        return text == reversed_text
      
