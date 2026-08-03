class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            days_used = 1
            load = 0
            
            for w in weights:
                if load + w > capacity:
                    days_used += 1
                    load = 0
                load += w

            return days_used <= days
        
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l + r) // 2

            if canShip(m):
                r = m 
            else:
                l = m + 1

        return l