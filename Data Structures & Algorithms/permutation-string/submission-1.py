class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(s1)
        for i in range(len(s2) - need + 1):
            curr = 0
            count2 = {}
            for j in range(i, i + need):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                curr += 1
                if curr == need:
                    return True
        return False