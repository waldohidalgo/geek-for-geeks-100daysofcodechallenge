class Solution:
    def numOfSubset(self, arr):
        # Your code goes here
        count=0
        arr.sort()
        n=len(arr)
        for i in range(n-1):
            if arr[i+1]-arr[i]>1:
                count+=1
        count+=1
        return count
    def numOfSubset2(self, arr):
        st=set(arr)
        for el in arr:
            if el-1 not in st:
                vl=el
                while vl+1 in st:
                    st.remove(vl+1)
                    vl+=1
        return len(st)


sol=Solution()
arr= [10, 100, 105]

print(sol.numOfSubset(arr[:]))
print(sol.numOfSubset2(arr[:]))
