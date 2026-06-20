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
# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remove=[]
        for i in nums:
            if i!=val:
                remove.append(i)
        nums[:]=remove
        return len(nums)
# 1394. Find Lucky Integer in an Array
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ak=[]
        for i in arr:
            if arr.count(i)==i:
                ak.append(i)
        if len(ak)==0:
            return -1
        return max(ak)            
    
# 412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i=n
        answer=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                answer.append("FizzBuzz")
            elif i%3==0:
                answer.append("Fizz")
            elif i%5==0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
# 326. Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        i = 0
        while 3**i <= n:
            if 3**i == n:
                return True
            i += 1

        return False

# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    
# 367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<1: return False
        return int(num**0.5)*int(num**0.5)==num
    
import pandas as pd

# 627. Swap Sex of Employees
def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex']=salary['sex'].map({"f":"m","m":"f"})
    return salary
# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sums=[]
        top=0
        for i in range(len(gain)):
            top+=gain[i]
            sums.append(top)
        if max(sums)<0:
            return 0
        return max(sums)
    
# 2540. Minimum Common Value
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        commons=[]
        nums1_set=set(nums1)
        nums2_set=set(nums2)
        for i in nums1_set:
            if i in nums2_set:
                commons.append(i)
        return min(commons) if commons else -1
 # 349. Intersection of Two Arrays   
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        commons=[]
        nums1_set=set(nums1)
        nums2_set=set(nums2)
        for i in nums1_set:
            if i in nums2_set:
                commons.append(i)
        return commons

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        commons1=[]
        commons2=[]
        nums1_set = set(nums1)
        nums2_set= set(nums2)
        for i in nums1_set:
            if i not in nums2_set:
                commons1.append(i)
        for i in nums2_set:
            if i not in nums1_set:
                commons2.append(i)
        return [commons1,commons2]
    

 # 350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        commons=[]
        for i in nums1:
            if i in nums2:
                commons.append(i)
                nums2.remove(i)
        
        return commons
# 2553. Separate the Digits in an Array  
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in nums:
            for k in str(i):
                answer.append(int(k))
        return answer