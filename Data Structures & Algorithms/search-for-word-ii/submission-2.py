class Node:
    
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # idea one:
        # build a trie of a word
        # see if that path exists
        # O(n^2*len(words)) time? nope this is wrong

        #how long does it take to see if a specific path exists 
        # O(n^4) as n^2 path seaches and then n^2 possible starts?
        

        #maybe convert graph to a trie?
        #then we can basically search the trie if a word exists
        #bingo

        #but then how do u start the trie?
        #do u start the trie at each node? how is this better?

        #building a tree usually  takes O(L) where L is num unique chars in string\

        #use backtracking to explore all paths of size ten starting from each node
        #as u add a node put it in the trie
        #then use the trie only to solve

        head = Node()
        # currNode = head

        NUM_ROWS = len(board)
        NUM_COLS = len(board[0])

        def dfs(row,col,pathLen,currNode):
            # print("enter", row, col, "pathLen =", pathLen)
            
            if row < 0 or row >= NUM_ROWS:
                return None
            if col < 0 or col>=NUM_COLS:
                return None
            if pathLen > 10: #any path longer than 10 we should stop searching
                return None
            if board[row][col] == "#": #overalapping not allowed
                return None
            
            saved = board[row][col]
            board[row][col] = "#"
            if saved not in currNode.children:
                currNode.children[saved] = Node()

            dfs(row+1,col,pathLen+1,currNode.children[saved])
            dfs(row-1,col,pathLen+1,currNode.children[saved])
            dfs(row,col+1,pathLen+1,currNode.children[saved])
            dfs(row,col-1,pathLen+1,currNode.children[saved])

            board[row][col] = saved
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                currNode = head
                dfs(i,j,0,currNode)
        
        #now to implement search
        def search(word,trieHead):
            curr = trieHead
            for c in word:
                if c not in curr.children:
                    print(c,"bad")
                    return False
                else:
                    curr = curr.children[c]
            return True
        
        res = []
        for word in words:
            if search(word,head):
                res.append(word)
        
        return res
