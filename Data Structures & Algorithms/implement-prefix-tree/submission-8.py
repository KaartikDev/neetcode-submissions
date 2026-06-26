class Node:
    def __init__(self, val = ""):
        self.val = val
        self.children = [None] * 26
        self.end = False

class PrefixTree:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        if word == "":
            return None
        
        i = 0
        currPointerSlot = ord(word[i]) - ord('a')
        currNode = self.head
        while i < len(word) and currNode.children[currPointerSlot]:
            # currPointerSlot = ord(word[i]) - ord('a')
            currNode = currNode.children[currPointerSlot]
            i+=1
            if i < len(word):
                currPointerSlot = ord(word[i]) - ord('a')
        
        for k in range(i,len(word)):
            currPointerSlot = ord(word[k]) - ord('a')
            # print("new char=", word[k])
            currNode.children[currPointerSlot] = Node(word[k])
            currNode = currNode.children[currPointerSlot]
        # print("end",currNode.val)
        currNode.end = True

    def search(self, word: str) -> bool:
        currNode = self.head
        i = 0
        currPointerSlot = ord(word[i]) - ord('a')
        while i < len(word) and currNode.children[currPointerSlot]:
            
            # print("curr char=", word[i])
            # print(currNode.val)
            currNode = currNode.children[currPointerSlot]
            i+=1
            if i < len(word):
                currPointerSlot = ord(word[i]) - ord('a')
        
        if currNode and currNode.end == True and i == len(word):
            # print(word,"FOUND",currNode.val,currNode.end)
            return True
        else:
            # print(word,"N/A",currNode.val,currNode.end)
            return False
        

    def startsWith(self, prefix: str) -> bool:
        
        currNode = self.head
        i = 0
        currPointerSlot = ord(prefix[i]) - ord('a')
        while i < len(prefix) and currNode.children[currPointerSlot]:
            # print("curr char=", prefix[i])
            # print(currNode.val)
            currNode = currNode.children[currPointerSlot]
            i+=1
            if i < len(prefix):
                currPointerSlot = ord(prefix[i]) - ord('a')
        
        if i == len(prefix):
            return True
        else:
            return False

        