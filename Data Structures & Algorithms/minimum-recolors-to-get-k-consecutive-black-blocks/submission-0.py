class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count = 0
        for i in range(k):
            if blocks[i] == "W":
                w_count += 1
        min_w = w_count

        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                w_count += 1
            if blocks[i-k] == "W":
                w_count -= 1
            min_w = min(min_w, w_count)
        return min_w