class Solution:
    def getSingle(self, arr):
        # code here 
        positive_bit_counts = [0] * 32
        negative_bit_counts = [0] * 32
        negative_count = 0

        for num in arr:
            if num >= 0:
                for i in range(32):
                    if (num >> i) & 1:
                        positive_bit_counts[i] += 1
            else:
                negative_count += 1
                abs_num = abs(num)
                for i in range(32):
                    if (abs_num >> i) & 1:
                        negative_bit_counts[i] += 1
                        
        result_abs = 0
        for i in range(32):
            if (positive_bit_counts[i] + negative_bit_counts[i]) % 3 != 0:
                result_abs |= (1 << i)

        if negative_count % 3 == 1:
            result = ~result_abs + 1
            return result
        else:
            return result_abs        

    def getSingle2(self,arr):
        # optimo
        once=0
        twice=0
        for num in arr:
            twice|=(once&num)
            once^=(num)
            mask_common=~(once&twice)
            once&=mask_common
            twice&=mask_common
        return once
    
    def getSingle3(self,arr):
        hs={}
        for num in arr:
            if num in hs:
                hs[num]+=1
                if hs[num]==3:
                    del hs[num]
            else:
                hs[num]=1
        return list(hs.keys())[0]

        
sol=Solution()
arr=  [-32,-19,-32,-32,4,4,4,5,5,5]
print(sol.getSingle2(arr))
