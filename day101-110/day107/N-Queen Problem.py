from typing import List
class Solution1:
    # tiempo n
    def _is_valid(self,row,i1,j1):
        for j2 in range(len(row)):
            i2=row[j2]-1
            if i1==i2 or abs(i1-i2)==abs(j1-j2):
                return False
        return True
    
    def nQueen(self, n):
        # code here
        res=[]

        def bt(row:List[int]):
            if len(row)==n:
                res.append(row[:])
                return
            for i in range(n):
                if self._is_valid(row,i,len(row)):
                    row.append(i+1)
                    bt(row)
                    row.pop()
        bt([])
        return res

class Solution2:    
    def nQueen(self, n):
        # code here
        res=[]
        s_row=set()
        s_diag_b=set()
        s_diag_u=set()
        
        def bt(row:List[int]):
            if len(row)==n:
                res.append(row[:])
                return
            for i in range(n):
                j=len(row)
                if i not in s_row and j-i not in s_diag_b and i+j not in s_diag_u :
                    row.append(i+1)
                    s_row.add(i)
                    s_diag_b.add(j-i)
                    s_diag_u.add(i+j)
                    bt(row)
                    row.pop()
                    s_row.remove(i)
                    s_diag_b.remove(j-i)
                    s_diag_u.remove(i+j)
        bt([])
        return res   

class Solution3:    
    def nQueen(self, n):
        # code here
        res=[]
        
        s_row:int=0
        s_diag_b:int=0
        s_diag_u:int=0
        
        def bt(row:List[int]):
            nonlocal s_row
            nonlocal s_diag_b
            nonlocal s_diag_u
            
            if len(row)==n:
                res.append(row[:])
                return
            for i in range(n):
                j=len(row)
                if not s_row&(1<<i) and not s_diag_b&(1<<(j-i+n)) and not s_diag_u&(1<<(i+j)):
                    row.append(i+1)
                    s_row|=(1<<i)
                    s_diag_b|=(1<<(j-i+n))
                    s_diag_u|=(1<<(i+j))
                    bt(row)
                    row.pop()
                    s_row&= ~(1 << i)
                    s_diag_b&=~(1<<(j-i+n))
                    s_diag_u&=~(1<<(i+j))   
        bt([])
        return res




sol=Solution2()
n = 4
print(sol.nQueen(n)) # [[1]]
    
