class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_freq = [0] * 26
        window_freq = [0] * 26

        # Build frequency arrays for s1 and the first window
        for i in range(n):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        if s1_freq == window_freq:
            return True

        # Slide the window across s2
        for i in range(n, m):
            window_freq[ord(s2[i]) - ord('a')] += 1         # Add new char
            window_freq[ord(s2[i - n]) - ord('a')] -= 1     # Remove old char
            if s1_freq == window_freq:
                return True

        return False