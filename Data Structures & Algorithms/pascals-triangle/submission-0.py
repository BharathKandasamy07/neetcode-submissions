class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        triangle = [[1], [1,1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(i - 1):
                res = triangle[-1][j] + triangle[-1][j + 1]
                row.append(res)
            row.append(1)
            triangle.append(row)
        return triangle