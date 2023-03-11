class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        
        if(m * n != r * c):
            return mat
            print('Hello')

        rows = []
        count = 0
        ans = []

        for i in range(m):
            for j in range(n):
                rows.append(mat[i][j])
                    #print(rows)
                count += 1 

                if(c == count):
                    ans.append(rows)
                    rows = []
                    count = 0

        return ans
