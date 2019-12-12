class Solution:
    def rotate(self, matrix):
        import math
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(math.ceil(len(matrix) / 2)):
            for j in range(i, len(matrix[i]) - 1 - i):
                print(i, j)
                old_index = [i, j]
                new_index = [j, len(matrix) - i - 1]
                old_tmp = matrix[old_index[0]][old_index[1]]
                new_tmp = matrix[new_index[0]][new_index[1]]
                matrix[new_index[0]][new_index[1]] = old_tmp
                old_index = new_index
                new_index = [old_index[1], len(matrix) - old_index[0] - 1]

                for _ in range(3):
                    old_tmp = new_tmp
                    new_tmp = matrix[new_index[0]][new_index[1]]
                    matrix[new_index[0]][new_index[1]] = old_tmp
                    old_index = new_index
                    new_index = [old_index[1], len(matrix) - old_index[0] - 1]