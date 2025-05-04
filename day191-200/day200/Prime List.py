
class Node:
    def __init__(self,x):
        self.val=x
        self.next=None


class Solution:
    def build(self,arr):
        dummy=Node(None)
        curr=dummy
        for i in range(len(arr)):
            curr.next=Node(arr[i])
            curr=curr.next
        return dummy.next

    def show(self,head):
        curr=head
        while curr:
            print(curr.val,end=' ')
            curr=curr.next
        print()

    def __get_max_value(self,head):
        max_val = 0
        current = head
        while current:
            max_val = max(max_val, current.val)
            current = current.next
        return max_val
    def __sieve(self, limit):
        is_prime=[True]*(limit+1)
        is_prime[0]=False
        is_prime[1]=False
        for i in range(2,limit+1):
            if is_prime[i]:
                for j in range(i*i,limit+1,i):
                    is_prime[j]=False
        return [i for i,prime in enumerate(is_prime) if prime]
    
    def __find_nearest_prime(self, num, primes):
        low=0
        high=len(primes)-1
        while low<=high:
            mid=(low+high)//2
            if primes[mid]>num:
                high=mid-1
            else:
                low=mid+1
        left=primes[low-1] if low>0 else float('inf')
        right=primes[low] if low<len(primes) else float('inf')

        if num-left<=right-num:
            return left
        else:
            return right


            
    
    def primeList(self, head):
        # code here
        primes=self.__sieve(self.__get_max_value(head)+100)
        current=head
        while current:
            if current.val==1:
                current.val=2
            else:
                current.val=self.__find_nearest_prime(current.val,primes)
            current=current.next
        return head


sol=Solution()
arr=[1,15,20]
head=sol.build(arr)
sol.show(sol.primeList(head))