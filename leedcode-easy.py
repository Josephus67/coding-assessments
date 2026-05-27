#125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for i in s:
            if i.isalnum():
                arr.append(i)
        if arr == arr[::-1]:
            return True
        return False