from typing import Dict,Optional

class Node:
    def __init__(self,value,key:Optional[int]=None,freq:Optional[int]=None):
        self.value=value
        self.prev:Optional["Node"]=None
        self.next:Optional["Node"]=None
        self.key=key
        self.freq=freq

class DLL:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0
    
    def delete_node(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
        self.size-=1
    
    def insert_node(self,node):
        last=self.tail.prev
        last.next=node
        node.prev=last
        node.next=self.tail
        self.tail.prev=node
        self.size+=1

    def _show(self):
        curr=self.head.next
        while curr!=self.tail:
            print("key1",curr.key,"act",curr.value,"prev",curr.prev.value,"next",curr.next.value)
            curr=curr.next

                    
class LFUCache:

    def __init__(self, cap: int):
        #code here
        self.cap=cap
        self.freq:Dict[int,DLL]={}
        self.keys:Dict[int,Node]={}
        self.min_freq=None

    def show(self):
        for k,v in self.freq.items():
            print("freq",k,"value")
            v._show()
            
    def _increment_freq(self,node:Node):
        prevDLL=self.freq[node.freq]
        prevDLL.delete_node(node)
        if prevDLL.size==0:
            del self.freq[node.freq]
            self.min_freq=self.min_freq+1 if self.min_freq==node.freq else self.min_freq
        node.freq+=1
        if node.freq in self.freq:
            currDLL=self.freq[node.freq]
            currDLL.insert_node(node)
        else:
            newDLL=DLL()
            newDLL.insert_node(node)
            self.freq[node.freq]=newDLL

    def _insert_free(self,node:Node):    
        if node.freq in self.freq:
            currDLL=self.freq[node.freq]
            currDLL.insert_node(node)
            self.keys[node.key]=node
        else:
            newDLL=DLL()
            newDLL.insert_node(node)
            self.freq[1]=newDLL
            self.keys[node.key]=node
            self.min_freq=1

    def get(self, key: int) -> int:
        #code here
        if key in self.keys:
            node=self.keys[key]
            self._increment_freq(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        #code here
        if key in self.keys:
            node=self.keys[key]
            node.value=value
            self._increment_freq(node)
            return
        node=Node(value,key,1)

        if self.cap==0:
            return
        
        size=len(self.keys)

        if size<self.cap:
            self._insert_free(node)
        else:
            minFreqDLL=self.freq[self.min_freq]
            sizeMinFreqDLL=minFreqDLL.size

            nodeDelete=minFreqDLL.head.next

            minFreqDLL.delete_node(nodeDelete)
            del self.keys[nodeDelete.key]

            if sizeMinFreqDLL==1:
                del self.freq[self.min_freq]
            self._insert_free(node)









cap=0
lfu=LFUCache(cap)
# lfu.put(1,1)
# lfu.put(2,2)
# print(lfu.get(1))
# lfu.put(3,3)
# print(lfu.get(2))
# lfu.put(4,4)
# print(lfu.get(3))
# print(lfu.get(4))
# lfu.put(5,5)

# lfu.show()

# cap=3
# lfu=LFUCache(cap)
# lfu.put(5,7)
# lfu.put(4,6)          
# lfu.put(3,5) 
# lfu.put(2,4)
# lfu.put(1,3) 
# print(lfu.get(1))
# print(lfu.get(2))
# print(lfu.get(3))
# print(lfu.get(4))
# print(lfu.get(5))
# lfu.show()

print(lfu.get(67))
lfu.put(82, 4)
lfu.put(1, 56)
lfu.put(29, 32)
lfu.put(51, 72)
print(lfu.get(6))
lfu.put(62, 87)
lfu.put(36, 34)
lfu.put(87, 27)
print(lfu.get(93))
print(lfu.get(6))
lfu.put(39, 70)
print(lfu.get(99))
print(lfu.get(16))
print(lfu.get(14))
print(lfu.get(47))
lfu.put(64, 63)
lfu.put(18, 81)
print(lfu.get(63))
print(lfu.get(54))
lfu.put(71, 63)
print(lfu.get(93))
print(lfu.get(30))
print(lfu.get(43))
print(lfu.get(87))
print(lfu.get(31))
lfu.put(87, 53)
print(lfu.get(64))
print(lfu.get(38))
lfu.put(60, 42)
print(lfu.get(63))
print(lfu.get(11))
lfu.put(75, 28)
