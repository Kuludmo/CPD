class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        t1, b1, l1, r1 = 0, n - 1, 0, m - 1
        t = 0
        ans = []

        while l1 <= r1 and t1 <= b1:
            if t == 0:
                j = l1
                while j <= r1:
                    ans.append(matrix[t1][j])
                    j += 1
                t += 1
                t1 += 1

            elif t == 1:
                j = t1
                while j <= b1:
                    ans.append(matrix[j][r1])
                    j += 1
                t += 1
                r1 -= 1

            elif t == 2:
                j = r1
                while j >= l1:
                    ans.append(matrix[b1][j])
                    j -= 1
                t += 1
                b1 -= 1

            else:
                j = b1
                while j >= t1:
                    ans.append(matrix[j][l1])
                    j -= 1
                t = 0
                l1 += 1

        return ans