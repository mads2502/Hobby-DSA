#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c,m):
    # Write your code here
    dp_table=[[0 for j in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp_table[i][j]=0
            if(j==0):
                dp_table[i][j]=1
    dp_table[0][0]=0
    ways=helper(n,c,m,dp_table)
    return ways
    
    
def helper(n,c,m,table):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(c[i-1]<=j):
                table[i][j]=table[i-1][j]+table[i][j-c[i-1]]
            else:
                table[i][j]=table[i-1][j]
    return table[m][n]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c,m)

    fptr.write(str(ways) + '\n')

    fptr.close()
