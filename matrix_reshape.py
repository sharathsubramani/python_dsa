class Solution:
    def matrixreshape(self, mat, r, c):
        old_rows = len(mat)
        old_cols = len(mat[0])
        no_of_ele = old_rows*old_cols
        new_reshape = r*c
        flatten =[]
        if new_reshape == no_of_ele:
            for num in mat:
                for ele in num:
                    flatten.append(ele)
        print(flatten)


if __name__ == '__main__':
    x = Solution()
    x.matrixreshape(
        [[0,  1,  2,  3],
         [4,  5,  6,  7],
            [8,  9,  10, 11]],4,3
    )
