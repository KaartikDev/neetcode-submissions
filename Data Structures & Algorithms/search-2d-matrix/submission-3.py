class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search col unil next row is bigger
        # then search row

        top = 0
        bottom = len(matrix)-1
        mid_h = (bottom + top)//2
        while top < bottom and matrix[mid_h][0] != target:
            # print(top,bottom,mid_h,matrix[mid_h][0])
            if target < matrix[mid_h][0]:
                bottom = mid_h-1
            else:
                top = mid_h+1
            mid_h = (bottom + top)//2

        if matrix[mid_h][0] > target and mid_h > 0: #fix off by one error (go to row below) as rows stricly increasing
            mid_h-=1
        
        # final_row = mid_h

        # print(top,bottom,mid_h,matrix[mid_h])
        l = 0
        r = len(matrix[mid_h])-1
        mid_w = (r+l)//2
        # i = 0
        while l < r and matrix[mid_h][mid_w] != target:
            # print(l,r,mid_w,matrix[mid_h][mid_w])
            if matrix[mid_h][mid_w] < target:
                l = mid_w+1
            else:
                r = mid_w-1
            mid_w = (r+l)//2
            # i+=1
        
        if matrix[mid_h][mid_w] == target:
            return True
        else:
            return False

        
            
