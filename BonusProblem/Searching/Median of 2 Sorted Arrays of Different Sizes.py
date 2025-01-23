class Solution:
    def medianOf2(self, a, b):
        #code here
        if len(a) > len(b):
            return self.medianOf2(b, a)
        
        n, m = len(a), len(b)
        k=-(-(n+m+1)//2)
        low, high = max(0, k - m), min(k, n)  
        
        while low <= high:
            cut_a = (low + high) // 2
            cut_b = k - cut_a  
            
            left_a = a[cut_a - 1] if cut_a > 0 else float('-inf')
            left_b = b[cut_b - 1] if cut_b > 0 else float('-inf')
            right_a = a[cut_a] if cut_a < n else float('inf')
            right_b = b[cut_b] if cut_b < m else float('inf')

            left_a_prev = a[cut_a - 2] if cut_a > 1 else float('-inf')  
            left_b_prev = b[cut_b - 2] if cut_b > 1 else float('-inf')
            
            if left_a <= right_b and left_b <= right_a:
                
                if (n+m)%2==0:
                    a=left_a if left_a>=left_b else left_b
                    b=max(left_b,left_a_prev)  if left_a>=left_b else max(left_a,left_b_prev)
                    return (a+b)/2
                else:
                    return max(left_a,left_b) 
            elif left_a > right_b:
                high = cut_a - 1  
            else:
                low = cut_a + 1   

        return -1 


# a = [-5, 3, 6, 12, 15]
# b = [-12, -10, -6, -3, 4, 10]
# a=[2, 3, 5, 8]
# b=[10, 12, 14, 16, 18, 20]
a=[1,2]
b=[3,4]
sol=Solution()
print(sol.medianOf2(a,b))