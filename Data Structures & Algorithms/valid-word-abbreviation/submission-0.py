class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # pointer for word
        j = 0  # pointer for abbreviation

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                # Leading zero is not allowed
                if abbr[j] == '0':
                    return False

                # Parse the full number
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                # Skip that many characters in word
                i += num
            else:
                # Letters must match exactly
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # Both pointers must reach the end
        return i == len(word) and j == len(abbr)