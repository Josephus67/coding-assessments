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