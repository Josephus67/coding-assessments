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