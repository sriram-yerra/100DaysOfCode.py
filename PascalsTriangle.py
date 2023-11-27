class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []

        # Initialize Pascal's Triangle with the first row
        triangle = [[1]]

        for i in range(1, numRows):
            # Calculate the current row based on the previous row
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)

            # Append the current row to the triangle
            triangle.append(row)

        return triangle

# Example usage:
numRows = 5
solution = Solution()
result = solution.generate(numRows)
print(result)
