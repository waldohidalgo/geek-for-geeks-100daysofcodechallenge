class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def uniqueCombinations1(self, arr, target):
        # code here
        res=set()
        n=len(arr)
        def comb(acum,k,seen):
            if acum==target:
                res.add(tuple(sorted(seen)))
                return
            if acum>target or k==n:
                return
            
            for i in range(k,n):
                # agregarlo
                seen.append(arr[i])
                acum+=arr[i]
                # nueva comb
                comb(acum,i+1,seen)
                # removerlo
                acum-=seen.pop()
        comb(0,0,[])
        return [list(tp) for tp in res]

    def uniqueCombinations2(self, arr, target):
        # code here
        res=[]
        arr.sort()
        n=len(arr)
        def comb(acum,k,seen):
            if acum==target:
                res.append(seen[:])
                return
            if acum>target or k==n:
                return
            
            for i in range(k,n):
                # agregarlo
                if i>k and arr[i]==arr[i-1]:
                    continue
                seen.append(arr[i])
                acum+=arr[i]
                # nueva comb
                comb(acum,i+1,seen)
                # removerlo
                acum-=seen.pop()
        comb(0,0,[])
        return res
    
sol=Solution()
# target=7
# arr=[1, 2, 3, 3, 5]
# arr=[5, 10, 15, 20, 25, 30]
# target=30
arr=[7,4,10,20,11,14,4,7,2,6,11,5,20,17,13,20,13]
target=16
print(sol.uniqueCombinations1(arr,target))
print(sol.uniqueCombinations2(arr,target))
 



