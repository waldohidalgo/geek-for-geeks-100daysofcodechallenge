class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n=len(s)
        l=0
        st=set()
        ct=0
        for i in range(n):
            if s[i] in st:
                ct=max(ct,len(st))
            while s[i] in st:
                st.remove(s[l])
                l+=1
            st.add(s[i])
        ct=max(ct,len(st))
        return ct


s="abcdefabcbb"
print(Solution().longestUniqueSubstr(s))