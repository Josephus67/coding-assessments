#125. Valid Palindrome
from ast import Add, List
import string


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
            
            
#3300. Minimum Element After Replacement With Digit Sum
class Solution:
    def minElement(self, nums: List[int]) -> int:
        counter = 0
        sums = []
        for num in nums:
            str_num = str(num)
            for i in str_num:
                counter+=int(i)
            sums.append(counter)
            counter = 0
        return min(sums)
    
# 1945. Sum of Digits of String After Convert
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alph=[]
        bets = string.ascii_lowercase
        string_digits=''
        for i in s:
            string_digits += str(bets.find(i)+1)
        for i in string_digits:
            alph.append(int(i))
        summation = sum(alph)
        alph_two = []
        for i in range(k-1):
            for dig in str(summation):
                alph_two.append(int(dig))
            summation = sum(alph_two)
            alph_two=[]
        return summation
    
#258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        while(num>9):
            arr = []
            for i in str(num):
                arr.append(int(i))
            num = sum(arr)
        return num

#2180. Count Integers With Even Digit Sum
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        digits=[]
        for i in range(1,num+1):
            for j in str(i):
                digits.append(int(j))
            if sum(digits)%2==0:
                count+=1
            digits=[]
        return count
    
#2574. Left and Right Sum Differences
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range(len(nums)):
            leftsum=sum(nums[:i])
            rightsum=sum(nums[i+1:])
            answer.append(abs(leftsum-rightsum))
        return answer

# 796. Rotate String
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        g_arr = []
        for i in s:
            g_arr.append(i)
        for i in range(len(s)):
            g_arr.append(g_arr[0])
            del g_arr[0]
            if ''.join(g_arr)==goal:
                return True
                break
        return False