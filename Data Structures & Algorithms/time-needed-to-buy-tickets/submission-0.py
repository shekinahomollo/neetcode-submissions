class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        cur = tickets[k]
        
        for i in range(k + 1):
            ans += min(tickets[i], cur)

        for i in range(k + 1, len(tickets)):
            ans += min(tickets[i], cur - 1)

        return ans