
#Subset sum problem
n=5
s=11
a=[2,3,7,8,10]
t=[['?' for j in range(s+1)] for i in range(n+1)]
def subsetsum():
    #initialise
    t[0][0]=1
    for i in range(n+1):
        for j in range(s+1):
            
            if i==0:
                t[i][j]=1
            if j==0:
                t[i][j]=0
          
    for i in range(1,n+1):
        for j in range(1,s+1):
            if a[i-1]<j:
                t[i][j]=((t[i-1][j-a[i-1]]) or (t[i-1][j]))
            else:
                t[i][j]=t[i-1][j]
    return t[n-1][s-1]
print(subsetsum())
print(t)
    
    

