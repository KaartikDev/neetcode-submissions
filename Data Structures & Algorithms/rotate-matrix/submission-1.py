class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #this is a transpostion
        for r in range(len(matrix)):
            for c in range(r+1,len(matrix[r])):
                
                temp = matrix[r][c]
                print(temp,matrix[c][r])
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
        #now to reverse each row
        for r in range(len(matrix)):
            matrix[r] = matrix[r][::-1]