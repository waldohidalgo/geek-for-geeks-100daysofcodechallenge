class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        def _is_valid_allocation(arr, n, k, max_pages):
            students = 1
            current_pages = 0

            for pages in arr:
                if current_pages + pages > max_pages:
                    students += 1
                    current_pages = pages
                    
                    if students > k:  
                        return False
                else:
                    current_pages += pages
            return True
        
        n = len(arr)
        if n<k:return -1
        l = max(arr)
        r = sum(arr)
        res=-1
        while l<=r:
            mid = (l+r)//2
            if _is_valid_allocation(arr, n, k, mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        
sol=Solution()
arr=[22, 23, 67]
k=1
print(sol.findPages(arr,k))