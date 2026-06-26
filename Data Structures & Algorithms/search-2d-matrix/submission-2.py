class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # M X N matrix where 1 >= M,N >= 100
        M = len(matrix)
        N = len(matrix[0])
        top = 0 
        bottom = len(matrix)-1

        while top < bottom:
            mid = top + int((bottom-top)/2)
            print(top, mid, bottom)
            if matrix[mid][N-1] == target: # need to check the N-1 entry in row as it is the largest in row
                return True
            
            if matrix[mid][0] <= target and matrix[mid][N-1] >= target: #the value is in the current row
                top = mid
                bottom = mid

            if matrix[mid][N-1] > target: #look at a different row
                bottom = mid-1
            else:
                top = mid+1
            
        #at this point top == bottom(found row to search)

        #now we search the row
        print(top,bottom)
        print(matrix[top])
        l = 0
        r = len(matrix[top]) -1

        while l <= r:
            mid = l + int((r-l)/2)

            if matrix[top][mid] == target:
                return True
            elif matrix[top][mid] > target:
                r = mid-1
            else:
                l = mid+1
        
        #if not found return False
        return False

        