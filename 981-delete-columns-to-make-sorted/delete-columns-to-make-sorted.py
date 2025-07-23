class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletecount = 0
        rows = len(strs)
        cols = len(strs[0])

        for col in range(cols):
            for row in range(1, rows):
                if strs[row][col] < strs[row - 1][col]:
                    deletecount += 1
                    break  

        return deletecount
        

        