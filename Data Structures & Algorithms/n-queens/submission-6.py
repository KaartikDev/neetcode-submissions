class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []

        if n == 1:
            return [["Q"]]


        def validBoard(board, row, col):
            if not board or not board[0]:
                print("ERROR PASSED IN EMPTY/MALFORMED BOARD")
                return None
            
            ROW_COUNT = len(board)
            COL_COUNT = len(board[0])

            if row >= ROW_COUNT or row < 0:
                print("OUT OF BOUNDS ROW")
                return None
            
            if col >= COL_COUNT or col < 0:
                print("OUT OF BOUNDS COL")
                return None
            
            #check left-right diaganol up
            cur_r = row-1
            cur_col = col-1
            while cur_col >= 0 and cur_r >= 0:
                if board[cur_r][cur_col] == "Q":
                    return False
                cur_r-=1
                cur_col-=1
            #check left-right diaganol down
            cur_r = row+1
            cur_col = col+1
            while cur_col < COL_COUNT and cur_r < ROW_COUNT:
                if board[cur_r][cur_col] == "Q":
                    return False
                cur_r+=1
                cur_col+=1
            #check right-left diagonal up
            cur_r = row-1
            cur_col = col+1
            while cur_col < COL_COUNT and cur_r >= 0:
                if board[cur_r][cur_col] == "Q":
                    return False
                cur_r-=1
                cur_col+=1
            #check right-left diagonal down
            cur_r = row+1
            cur_col = col-1
            while cur_col >= 0 and cur_r < ROW_COUNT:
                if board[cur_r][cur_col] == "Q":
                    return False
                cur_r+=1
                cur_col-=1

            
            return True
        
        #how many possible permutations are their of chessboards with n queens on them?
        # (nxn) P n --> n^2 total slots and we choose n and order does matter
        # with max n being 8, we could generate 64P8 boards and then do n^2 work on each to filter (O(n) search for each queen's sight)


        # looking at given examples we know queens must alternate rows and columns
        
        #lets try the above brute force way first --> generate n^2 64P8 boards and filter...nope thats over 10^13
        #cant explore all possible solutions

        # how can we cut number of permutatios down? only one queen per row?
        # nP1 * n? ==> n*2 options? thats much more reasonable. Let's write this code


        #final startegy
        #build n strings which repersent rows, with the queen in a different spot each time. 
        #find unqiue permutations of those n rows, only add to res if entire board valid via vlaid board checker
        #valid board checker only needs to check diagonals
        
        
        
        
        tempRowList = ["."]*n
        rowOptions = []
        for i in range(n):
            
            tempRowList[i] = 'Q'
            rowOptions.append("".join(tempRowList))
            # print(tempRowList)
            tempRowList[i] = '.'
            
        
        # return None
        #now build permutations with these rows
        
        chosenArr = [False] * n
        goodBoardPerms = []
        currBoard = []
        def dfs_row_perm():
            if len(currBoard) == n:
                #quick valid check:
                # for r in range(n):
                #     for c in range(n):
                #         if currBoard[r][c] =="Q" and not validBoard(currBoard, r, c):
                #             return None
                #all spots valid
                goodBoardPerms.append(currBoard.copy())
                # print(currBoard)
                return None
            
            for j in range(len(chosenArr)):
                if not chosenArr[j]:
                    chosenArr[j] = True
                    currBoard.append(rowOptions[j])
                    mostRecentRow = len(currBoard)-1
                    mostRecentCol = j
                    if validBoard(currBoard, mostRecentRow, mostRecentCol):
                        dfs_row_perm()
                    currBoard.pop()
                    chosenArr[j] = False
        
        dfs_row_perm()

        return goodBoardPerms
        
        # goodBoards = []
        # for board in allBoardPerms:
        #     entireBoardCorrect = True
        #     for row in range(len(board)):
        #         for col in range(len(board[0])):
        #             if board[row][col] == "Q" and entireBoardCorrect and not validBoard(board, row, col):
        #                 # print("GOOD")
        #                 entireBoardCorrect = False
        #     if entireBoardCorrect:
        #         # print(board)
        #         goodBoards.append(board)
            
        # return goodBoards

            
            
                            
        
        # print(goodBoards)

        # def validBoard(board, row, col):
        #     if not board or not board[0]:
        #         print("ERROR PASSED IN EMPTY/MALFORMED BOARD")
        #         return None
            
        #     ROW_COUNT = len(board)
        #     COL_COUNT = len(board[0])

        #     if row >= ROW_COUNT or row < 0:
        #         print("OUT OF BOUNDS ROW")
        #         return None
            
        #     if col >= COL_COUNT or col < 0:
        #         print("OUT OF BOUNDS COL")
        #         return None

        #     #dont need to check row or col cuz of the way generated 

        #     # #check below
        #     # for cur_r in range(row+1,ROW_COUNT):
        #     #     if board[cur_r][col] == "Q":
        #     #         return False
            
        #     # #check above
        #     # cur_r = 0
        #     # while cur_r < row:
        #     #     if board[cur_r][col] == "Q":
        #     #         return False
        #     #     cur_r+=1
            
        #     # #check right
        #     # for cur_col in range(col+1,COL_COUNT):
        #     #     if board[row][cur_col] == "Q":
        #     #         return False
                
            
        #     # #check left
        #     # cur_col = 0
        #     # while cur_col < col:
        #     #     if board[row][cur_col] == "Q":
        #     #         return False
        #     #     cur_col+=1
            


        #     #check left-right diagonal up
        #     cur_r = row-1
        #     cur_col = col-1
        #     while cur_col >= 0 and cur_r >= 0:
        #         if board[cur_r][cur_col] == "Q":
        #             return False
        #         cur_r-=1
        #         cur_col-=1
        #     #check left diaganol down
        #     cur_r = row+1
        #     cur_col = col+1
        #     while cur_col < COL_COUNT and cur_r < ROW_COUNT:
        #         if board[cur_r][cur_col] == "Q":
        #             return False
        #         cur_r+=1
        #         cur_col+=1
            
        #     #check right-left diagonal up
        #     cur_r = row-1
        #     cur_col = col+1
        #     while cur_col < COL_COUNT and cur_r >= 0:
        #         if board[cur_r][cur_col] == "Q":
        #             return False
        #         cur_r-=1
        #         cur_col+=1
            
        #     #check right-left diagonal down
        #     cur_r = row+1
        #     cur_col = col-1
        #     while cur_col >= 0 and cur_r < ROW_COUNT:
        #         if board[cur_r][cur_col] == "Q":
        #             return False
        #         cur_r+=1
        #         cur_col-=1

            
        #     return True






