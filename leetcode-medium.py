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
    
# 686. Repeated String Match
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        catch = (len(b) + len(a) - 1) // len(a) 
        for i in range(catch,catch+3):
            look = a*i
            if b in look:
                return i
        return -1

# 1344. Angle Between Hands of a Clock 
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        diff = abs(hour_angle - minute_angle)
        
        return min(diff, 360 - diff)


# 1833. Maximum Ice Cream Bars
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counter=0
        cost_s=sorted(costs)
        for i in cost_s:
            if i<=coins:
                counter+=1
                coins-=i
        return counter