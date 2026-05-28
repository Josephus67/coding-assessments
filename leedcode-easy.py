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
    
#389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if char not in s:
                return char
            if s.count(char)< t.count(char):
                return char