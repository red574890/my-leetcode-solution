class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        ans = 0
        i = 0  # heater pointer
        for h in houses:
            # Move heater pointer to the closest one to current house
            while i + 1 < len(heaters) and abs(heaters[i+1] - h) <= abs(heaters[i] - h):
                i += 1
            ans = max(ans, abs(heaters[i] - h))
        
        return ans
