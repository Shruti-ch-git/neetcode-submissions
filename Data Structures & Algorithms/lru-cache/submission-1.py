class Node:
    def __init__(self, key, val ):
        self.key, self.val= key, val
        self.prev= self.next= None
         
class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} #to map the keys to their nodes #hashmap
        self.left, self.right = Node(0,0), Node(0,0) # ll
        #2 pointer, begin and end
        self.left.next, self.right.prev= self.right, self.left
    
    def remove(self, node):
        prv = node.prev # double linked list
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
      
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]= Node(key,value)
        self.insert(self.cache[key])
        while len(self.cache)> self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            

        
        
