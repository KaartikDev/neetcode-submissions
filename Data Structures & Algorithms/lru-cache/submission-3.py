class Node:
    def __init__(self, key,val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # least recenetly used....aka oldest
        # index used queue
        
        self.nodeMap = {} #key, address

        self.head = None # most recently used
        self.tail = None # oldest node
        self.size = capacity
        # self.data = [-1]*self.size
    
    def insert_head(self,p):
        if not self.head:
            self.head = p
            self.tail = p   
            p.prev = None
            p.next = None
        else:
            self.head.prev = p
            p.next = self.head
            p.prev = None #safety
            self.head = p
    
    def remove(self,p):

        if not self.head or not self.tail: #both the tail and head must exist to remove
            return
        
        if p == self.head and p == self.tail: #only one node
            self.head = None
            self.tail = None

        if p == self.tail: #remove tail
            self.tail = p.prev #move tail back
            if self.tail:
                self.tail.next = None #disconnect
            p.prev = None
            p.next = None #safety
        elif p == self.head:
            
            self.head = p.next #move head forward
            if self.head:
                self.head.prev = None 
            p.prev = None #safety
            p.next = None
        else:
            prev_node = p.prev
            next_node = p.next
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
            p.next = None
            p.prev = None


    def get(self, key: int) -> int:
        # print(key-1)

        if key not in self.nodeMap:
            return -1
        
        p = self.nodeMap[key]
        self.remove(p)
        self.insert_head(p)

        return self.head.val 

    def put(self, key: int, value: int) -> None:
        #existing code
        if key in self.nodeMap:
            #need to put at fornt of linked list as we just updated it
            p = self.nodeMap[key]
            p.val = value
            if not p:
                return None #something wne wrong here....
            self.remove(p)
            self.insert_head(p)
            return


        #new
        new_node = Node(key,value)
        if len(self.nodeMap) == self.size:
            # we must delete the tail append to head and update valueMap
            old_tail_key = self.tail.key
            
            
            self.remove(self.tail)
            self.nodeMap.pop(old_tail_key,None)

            # add in new node
            self.insert_head(new_node)
            self.nodeMap[key]=new_node
        else:
            # we can just add to head
            # self.remove(p)
            self.insert_head(new_node)
            self.nodeMap[key]=new_node
        return None

        
