class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.head = Node()
        

    def addWord(self, word: str) -> None:
        currNode = self.head
        for c in word:
            # print("curr letter=",c)
            if c not in currNode.children:
                # print("adding letter",c)
                currNode.children[c] = Node()
                # print(currNode.children)
                currNode = currNode.children[c]
            else:
                currNode = currNode.children[c]
            
        currNode.end = True #one after last letter!
    

        

    def search(self, word: str) -> bool:
        #push all possible paths onto a stakc and do stakc besed dfs
        
        pathsToExplore = [(0,self.head)]

        while pathsToExplore:
            i,currNode = pathsToExplore.pop()
            assert i <= len(word), "too large index something went wrong"

            if i == len(word):
                if currNode.end:
                    return True
                else: #skip this path if used up length and not end
                    continue
            
            # print(i,word[i],currNode.children)
            c = word[i]
            if c == '.':
                for letters in currNode.children:
                    pathsToExplore.append((i+1,currNode.children[letters]))
            elif c in currNode.children:
                pathsToExplore.append((i+1,currNode.children[c]))
            
        return False


        
                
        
