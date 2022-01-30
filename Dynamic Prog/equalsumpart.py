'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")

a=[2,3,7,8,10]

def subsetsum(s,n):
    t=[['?' for j in range(s+1)] for i in range(n+1)]
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
    
def equalpartsum(n):
    if(sum(a)%2!=0):
        return 0 
    else:
        return subsetsum(sum(a)//2,n)
n=5
s=11
print(subsetsum(s,n))
print(equalpartsum(n))

    
    

