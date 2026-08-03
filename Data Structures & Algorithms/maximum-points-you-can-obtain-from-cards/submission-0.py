class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        score = sum(cardPoints[:k])
        max_score = score
        for i in range(1, k+1):
            score -= cardPoints[k-i]
            score += cardPoints[n-i]
            max_score = max(max_score, score)
        return max_score