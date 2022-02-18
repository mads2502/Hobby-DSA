
'''You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_table=[[0 for i in range(amount+1)]for _ in range(len(coins)+1)]
        #initialisation first row and column
        for j in range(amount+1):
            dp_table[0][j]=math.inf-1#no of coins<required sum i.e coins=0
        for i in range(len(coins)+1):
            dp_table[i][0]=0
        #initialising second row
        for j in range(1,amount+1):
            if j % coins[0]==0:
                dp_table[1][j]=j//coins[0]
            else:
                dp_table[1][j]=math.inf-1
        #helper to implement dp
        val=self.helper(dp_table,coins,amount)
        if(val==math.inf):
            return -1
        else:
            return val
    
    def helper(self,table,coins,amt):
        
        for i in range(2,len(coins)+1):
            for j in range(1,amt+1):
                if coins[i-1]<=j:
                    table[i][j]=min(0+table[i-1][j],1+table[i][j-coins[i-1]])#adding 1 for noof 
                    #coins
                else:
                    table[i][j]=table[i-1][j]
        return table[len(coins)][amt]
        
        
        
        
