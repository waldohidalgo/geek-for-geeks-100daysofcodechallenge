class Solution:
    def mergeArrays(self, a, b):
        # code here
        n, m = len(a), len(b)
        gap = (n + m + 1) // 2  
        
        def next_gap(g):
            if g <= 1:
                return 0
            return (g + 1) // 2
        
        while gap > 0:
            i, j = 0, gap
            
            while j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                i += 1
                j += 1
            
            j -= n
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
        
            i -= n
            while j < m:
                if b[i] > b[j]:
                    b[i], b[j] = b[j], b[i]
                i += 1
                j += 1
        
            gap = next_gap(gap)

a = [2, 4, 7, 10]
b = [2, 3]

Solution().mergeArrays(a, b)
print("a:", a)  # Debería contener los primeros n elementos ordenados
print("b:", b)  # Debería contener los últimos m elementos ordenados