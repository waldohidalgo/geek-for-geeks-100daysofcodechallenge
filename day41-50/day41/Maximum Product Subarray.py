class Solution:
	
	
    def maxProduct(self,arr):
		
        n = len(arr)
        ans=arr[0]
        pmax=arr[0]
        pmin=arr[0]
        for i in range(1,n):
            if arr[i]<0:
                pmax,pmin=pmin,pmax
            pmax=max(pmax*arr[i],arr[i])
            pmin=min(pmin*arr[i],arr[i])
            ans=max(ans,pmax)
        return ans

    def maxProduct2(self,arr):
        # este enfoque resuelve el problema pero el hecho de mantener los positivos y negativos agrega complejidad adicional innecesaria ya que basta con llevar un registro de maximos y minimos
        n=len(arr)
        ans=arr[0]
        pos=None
        neg=None
        for i in range(n):
            if arr[i]==0:
                pos=None
                neg=None
                ans=max(ans,0)
                continue

            if pos is None and neg is None:
                if arr[i]>0:
                    pos=arr[i]
                    ans=max(ans,pos)
                else:
                    neg=arr[i]
                    ans=max(ans,neg)
            elif pos is None:
                if arr[i]>0:
                    pos=arr[i]
                    neg=neg*arr[i]
                    ans=max(ans,pos)
                else:
                    pos,neg=neg*arr[i],arr[i]
                    ans=max(ans,pos)
            elif neg is None:
                if arr[i]>0:
                    pos=pos*arr[i]
                    ans=max(ans,pos)
                else:
                    neg=pos*arr[i]
                    pos=None
                    ans=max(ans,arr[i])
            else:
                if arr[i]>0:
                    pos,neg=pos*arr[i],neg*arr[i] 
                else:
                    pos,neg=neg*arr[i],pos*arr[i]                       
                ans=max(ans,pos)    
        return ans    
    def maxProduct3(self,arr):        
        n = len(arr)
        ans = arr[0]  
        pos, neg = 1, 1  
        for i in range(n):
            if arr[i] == 0:    
                pos, neg = 1, 1
                ans = max(ans, 0)
            else:       
                temp_pos = max(arr[i], pos * arr[i], neg * arr[i])
                neg = min(arr[i], pos * arr[i], neg * arr[i])
                pos = temp_pos     
                ans = max(ans, pos)
        return ans   
sol=Solution()


arr=[2, 3, 4,0,-2, -3, -10, 0, 60] 
print(sol.maxProduct(arr))
print(sol.maxProduct2(arr))
print(sol.maxProduct3(arr))

