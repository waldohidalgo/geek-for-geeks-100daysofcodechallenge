from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        #code here
        values=defaultdict(list)
        for el in arr:
            word=''.join(sorted(el))
            values[word].append(el)
        return list(values.values())
    
sol=Solution()
arr=["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"]
print(sol.anagrams(arr))