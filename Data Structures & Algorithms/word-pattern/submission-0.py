class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        hashmap1 = {}
        hashmap2 = {}

        for c, w in zip(pattern, words):
            if c in hashmap1 and hashmap1[c] != w:
                return False
            if w in hashmap2 and hashmap2[w] != c:
                return False
            hashmap1[c] = w
            hashmap2[w] = c
        return True