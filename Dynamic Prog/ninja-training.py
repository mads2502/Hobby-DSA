from typing import *

  '''
  You are given a 2D array of size N*3 ‘POINTS’ with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.
  '''
  
def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
 
    dp_table=[[-1 for j in range(4)]for i in range(n+1)]
    res1=helper(n,points,1,dp_table)
    res2=helper(n,points,2,dp_table)
    res3=helper(n,points,3,dp_table)
    
    
    return max(res1,res2,res3)
def helper(n,pts,i,dp):
    if n==0:
        return 0
    #computing for the successive days 
    if dp[n][i]!=-1:
        return dp[n][i]
    else:
        val=0
        a=-1
        point=pts[n-1][i-1]#points for the ith task on nth day
        #for the prev day
        if i==1:
            a=max(helper(n-1,pts,2,dp),helper(n-1,pts,3,dp))
        elif i==2:
            a=max(helper(n-1,pts,1,dp),helper(n-1,pts,3,dp))
        else:
            a=max(helper(n-1,pts,1,dp),helper(n-1,pts,2,dp))
        val=a+point
        dp[n][i]=val
        return dp[n][i]
            
        

