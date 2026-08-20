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
    
    def remove(self,p): # deletes p from doubly linked list

        if not self.head or not self.tail: #both the tail and head must exist to remove
            return
        
        if p == self.head and p == self.tail: #only one node
            self.head = None #reset to empy statire
            self.tail = None
        
        elif p == self.tail: #delete oldest node at tail
            self.tail = p.prev #move tail back to one before
            self.tail.next = None #disconnect forward, always exist as garunteed  len(DLL)>1
            p.prev = None #disconnect backward, always exist as garunteed  len(DLL)>1
            p.next = None #safety, not needed
        
        elif p == self.head: #delete newest node
            self.head = p.next #move head forward
            self.head.prev = None #disconnet backward dir
            p.prev = None #safety
            p.next = None #disconnect forward dir
        
        else: #delete somewhere in middle
            prev_node = p.prev
            next_node = p.next
            
            # No none checks needed, we know these aren't None
            prev_node.next = next_node
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
        #existing in LRU
        if key in self.nodeMap:
            #need to put at fornt of linked list as we just updated it
            p = self.nodeMap[key]
            p.val = value
            if not p:
                return None #something wne wrong here....
            self.remove(p)
            self.insert_head(p)
            return


        #NOT existing in LRU
        new_node = Node(key,value)
        if len(self.nodeMap) == self.size:
            # we must delete the tail append to head and update valueMap
            old_tail_key = self.tail.key
            
            
            self.remove(self.tail)
            del self.nodeMap[old_tail_key]

            # add in new node
            self.insert_head(new_node)
            self.nodeMap[key]=new_node
        else:
            # we can just add to head
            self.insert_head(new_node)
            self.nodeMap[key]=new_node
        return None

        
