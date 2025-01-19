def rotate(mat): 
    #code here
    n=len(mat)
    if n==1:
        return mat
    #transpose
    for i in range(n):
        for j in range(i):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
    #reverse
    for i in range(n):
        for j in range(n//2):
            mat[i][j],mat[i][n-j-1]=mat[i][n-j-1],mat[i][j]
    return mat

mat=[[1]]
print(rotate(mat))
        