#2126. Destroying Asteroids
from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass<asteroid:
                return False
            mass+=asteroid
        return True

        #if mass+sum(asteroids)-max(asteroids)>=max(asteroids):
         #   return True
        #return False

# 3689. Maximum Total Subarray Value I     
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums)-min(nums))*k

# 3612. Process String with Special Operations I
class Solution:
    def processStr(self, s: str) -> str:
        import string
        result=[]
        for i in s:
            if i in list(string.ascii_lowercase):
                result.append(i)
            elif i=='*':
                if len(result)>0:
                    result.pop(-1)
            elif i=='#':
                cp=result.copy()
                result.extend(cp)
            elif i=='%':
                result.reverse()
        return ''.join(result)