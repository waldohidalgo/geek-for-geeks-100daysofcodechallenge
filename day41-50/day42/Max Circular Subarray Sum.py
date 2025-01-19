def circularSubarraySum(arr):
    ##Your code here
    n=len(arr)
    max_sum=arr[0]
    curr_max_sum=arr[0]
    curr_min_sum=arr[0]
    min_sum=arr[0]
    total_sum=arr[0]
    for i in range(1,n):
        total_sum+=arr[i]
        curr_max_sum=max(arr[i],curr_max_sum+arr[i])
        max_sum=max(curr_max_sum,max_sum)
        curr_min_sum=min(arr[i],curr_min_sum+arr[i])
        min_sum=min(curr_min_sum,min_sum)
    
    return max(max_sum,total_sum-min_sum)


#arr=[8, -8, 9, -9, 10, -11, 12]
#arr=[10, -3, -4, 7, 6, 5, -4, -1]
arr=[-1, 40, -14, 7, 6, 5, -4, -1] 
print(circularSubarraySum(arr))
