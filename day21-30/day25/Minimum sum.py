

class Solution:
    def minSum(self, arr):
        arr.sort()  
        num1=""
        num2=""
        res=""
        n=len(arr)
        for i in range(n):
            if i%2==0:
                num1+=str(arr[i])
            else:
                num2+=str(arr[i])
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            carry = total // 10  
            res+=str(total % 10) 

            i -= 1
            j -= 1    

        res=res[::-1]
    
        return res.lstrip('0')   
        
    

        
        
        
        

    
sol=Solution()
#arr= [6, 8, 4, 5, 2, 3]
#arr=[5, 3, 0, 7, 4]
#arr=[0,1,0,1,0,1,0,0,0]
#arr=[3,7,2]
arr = [7, 0, 8, 9, 3, 3, 9, 2, 9, 1, 5, 6, 7, 9, 4, 3, 9, 5, 5, 8, 7, 8, 0, 2, 5, 7, 3, 6, 8, 3, 6, 9, 9, 3, 0, 3, 3, 7, 8, 7, 0, 5, 4, 3, 6, 2, 4, 9, 9, 6, 7, 3, 1, 0, 9, 4, 1, 2, 5, 8, 3, 6, 3, 6, 3, 9, 5, 0, 5, 3, 8, 2, 6, 6, 1, 2, 6, 9, 2, 7, 3, 9, 3, 9, 0, 8, 8, 1, 6, 9, 0, 0, 6, 7, 1, 1, 1, 0, 6, 5, 4, 3, 8, 6, 1, 3, 3, 2, 7, 4, 1, 4, 5, 5, 8, 0, 6, 3, 5, 8, 4, 7, 4, 1, 7, 9, 5, 1, 5, 4, 0, 1, 8, 6, 8, 0, 7, 2, 6, 9, 1, 9, 0, 1, 9, 1, 8, 5, 5, 0, 0, 6, 3, 3, 8, 8, 0, 5, 0, 8, 3, 9, 5, 8, 6, 7, 1, 3, 4, 5, 9, 8, 4, 6, 9, 8, 5, 8, 5, 3, 7, 7, 8, 7, 3, 6, 4, 7, 8, 4, 5, 7, 5, 7, 6, 4, 2, 6, 1, 0, 3, 5, 5, 3, 9, 6, 7, 5, 3, 9, 4, 9, 4, 3, 9, 5, 6, 7, 8, 0, 8, 8, 8, 6, 1, 1, 1, 2, 9, 6, 0, 3, 3, 5, 7, 1, 9, 0, 6, 1, 5, 4, 9, 5, 3, 6, 2, 9, 4, 7, 1, 0, 8, 7, 7, 2, 6, 0, 9, 3, 4, 5, 8, 3, 9, 0, 6, 2, 1, 0, 5, 7, 2, 2, 3, 5, 2, 5, 0, 0, 5, 9, 0, 0, 9, 0, 9, 4, 9, 5, 9, 2, 1, 3, 6, 0, 0, 9, 0, 2, 1, 2, 5, 6, 8, 1, 0, 7, 4, 4, 6, 4, 4, 6, 2, 6, 0, 0, 4, 0, 3, 9, 9, 5, 6, 1, 7, 5, 8, 2, 5, 1, 3, 4, 6, 4, 4, 4, 3, 3, 7, 6, 8, 1, 4, 7, 3, 5, 2, 6, 1, 6, 9, 3, 0, 8, 0, 9, 5, 3, 5, 4, 2, 9, 5, 0, 5, 7, 2, 1, 1, 8, 8, 1, 7, 8, 3, 4, 9, 9, 9, 1, 3, 8, 9, 4, 7, 8, 7, 6, 5, 4, 4, 9, 4, 9, 3, 1, 8, 5, 8, 7, 0, 0, 8, 7, 7, 3, 2, 6, 8, 4, 8, 2, 1, 7, 8, 2, 6, 0, 4, 9, 7, 5, 8, 1, 9, 2, 3, 8, 7, 7, 1, 7, 7, 1, 2, 3, 8, 4, 8, 3, 7, 4, 5, 9, 8, 8, 4, 4, 3, 6, 2, 5, 9, 0, 2, 2, 2, 6, 1, 9, 5, 7, 0, 0, 2, 1, 2, 7, 7, 8, 1, 4, 0, 1, 4, 5, 4, 9, 3, 5, 1, 2, 9, 9, 8, 3, 1, 6, 3]

print(sol.minSum(arr))