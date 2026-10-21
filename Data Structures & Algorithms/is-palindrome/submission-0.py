class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_join="".join(char.lower() for char in s if char.isalnum())
        s_reversed=(s_join[::-1])
        return s_join==s_reversed
        