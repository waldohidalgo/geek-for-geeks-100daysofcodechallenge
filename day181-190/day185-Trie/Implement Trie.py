class Trie:
    def __init__(self):
        # implement Trie
        self.root = {}
        
    def insert(self, word: str):
       # insert word into Trie
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
         # search word in the Trie
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '#' in node

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return True
    

def query(num,word,trie:Trie):
    if num==1:
        trie.insert(word)
    elif num==2:
        return (trie.search(word))
    else:
        return (trie.isPrefix(word))
    

trie = Trie()
queries =[[1, "gfg"], [1, "geeks"], [3, "fg"], [3, "geek"], [2, "for"]]
res=[]
for num,word in queries:
    if num!=1:
        res.append(query(num,word,trie))
    else:
        query(num,word,trie)

print(res)
