class Solution:
    def maxPartitions(self , s):
        # code here
        arr=[-1]*26
        for i,c in enumerate(s):
            arr[ord(c)-97]=max(arr[ord(c)-97],i)
        max_index=-1
        count=0
        for i,c in enumerate(s):
            max_index=max(max_index,arr[ord(c)-97])
            if max_index==i:
                count+=1
                max_index=-1
        return count

    def maxPartitions2(self , s):
        # code here
        hs={}
        for i,c in enumerate(s):
            if c in hs:
                hs[c]=max(hs[c],i)
            else:
                hs[c]=i
        max_index=-1
        count=0
        for i,c in enumerate(s):
            max_index=max(max_index,hs[c])
            if max_index==i:
                count+=1
                max_index=-1
        return count


sol=Solution()
#s = "ababcbacadefegdehijhklij"
#s = "aaa"
s = "acbbcc"
print(sol.maxPartitions2(s))
