class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = sorted(x for x, y in points)
        result = 0
        for i in range(1, len(ans)):
            width = ans[i] - ans[i-1]
            result = max(result, width)
        return result