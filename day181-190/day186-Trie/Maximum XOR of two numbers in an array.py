class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node:
                node[bit] = {}
            node = node[bit]

    def maxXor(self, num):
        node = self.root
        ans = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit ^ 1 in node:
                ans |= 1 << i
                node = node[bit ^ 1]
            else:
                node = node[bit]
        return ans


class Solution:
    def maxXor(self, arr):
        #code here
        trie = Trie()
        for num in arr:
            trie.insert(num)
        res = 0
        for num in arr:
            res = max(res, trie.maxXor(num))
        return res
    

sol=Solution()
arr= [1, 2, 3, 4, 5, 6, 7]
print(sol.maxXor(arr))