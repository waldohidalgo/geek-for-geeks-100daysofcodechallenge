class Node:
    def __init__(self,value,key=None):
        self.value=value
        self.prev=None
        self.next=None
        self.key=key

class DLL:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def delete_node(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
    
    def insert_node(self,node):
        last=self.tail.prev
        last.next=node
        node.prev=last
        node.next=self.tail
        self.tail.prev=node

    def _show(self):
        curr=self.head.next
        while curr!=self.tail:
            print("key",curr.key,"act",curr.value,"prev",curr.prev.value,"next",curr.next.value)
            curr=curr.next



class LRUCache:
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.cap=cap
        self.hs={}
        self.dll=DLL()
            
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.hs:
            node=self.hs[key]
            self.dll.delete_node(node)
            self.dll.insert_node(node)
            return node.value
        return -1
   
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        size=len(self.hs)
        if key in self.hs:
            node=self.hs[key]
            node.value=value
            self.dll.delete_node(node)
            self.dll.insert_node(node)
            return  
        node=Node(value,key)    

        if size>=self.cap:
            last=self.dll.head.next
            lastKey=last.key
            del self.hs[lastKey]
            self.dll.delete_node(last)

        self.dll.insert_node(node)
        self.hs[key]=node
        

cap=2
lru=LRUCache(cap)
# lru.put(1,2)
# print(lru.get(1))
# lru.dll._show()

# lru.put(4,4)
# lru.put(3,3)
# lru.put(2,2)
# lru.put(1,1)
# print(lru.get(1))
# print(lru.get(2))
# print(lru.get(3))
# print(lru.get(4))
# lru.dll._show()

# lru.dll._show()


lru.put(1,2)
lru.put(2,3)
lru.put(1,5)
lru.put(4,5)
lru.put(6,7)
print(lru.get(4))
lru.put(1,2)
print(lru.get(3))
lru.dll._show()