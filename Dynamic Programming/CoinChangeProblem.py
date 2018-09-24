import sys

# Using Dynamic Programming
def coinChangeDP(coins, amount):
    memo = [[-1 for x in range(amount+1)] for y in range(len(coins))]
    
    for j in range(amount+1):
        memo[0][j] = int(j / coins[0])
    
    for i in range(1,len(coins)):
        for j in range(len(memo[i])):
            
            if j == 0:
                memo[i][j] = 0
            
            elif j > 0:
                if coins[i] <= j:
                    memo[i][j] = min(memo[i-1][j], 1 + memo[i][j - coins[i]])
                else:
                    memo[i][j] = memo[i-1][j]
    print(memo)
    
    # To print number of coins required for amount
    print(memo[len(coins)-1][amount])
    
    # To print the coins needed for amount
    i = len(coins) - 1
    j = amount
    temp = []
    while(i > 0):
        if memo[i][j] != memo[i-1][j]:
            temp.append(coins[i])
            j = j - coins[i]
            i -= 1
        else:
            i -= 1
    if memo[i][j] > 0:
        temp.append(coins[i])
    print(temp)
        

# Using DP with only one array
def coinChangeDP1(coins, amount):
    memo         = [int(sys.maxsize) for x in range(amount+1)]
    memo[0]      = 0
    coinLocation = [-1 for x in range(amount+1)]
    
    for i in range(len(coins)):
        for j in range(coins[i],amount+1,1):
            if 1 + memo[j-coins[i]] < memo[j]:
                memo[j]         = 1 + memo[j-coins[i]]
                coinLocation[j] = i 
    
    # Print number of coins required for amount
    print(memo[amount])
    
    # Print coins for amount
    i    = amount
    temp = []
    while i != 0:
        temp.append(coins[coinLocation[i]])
        i = i - coins[ coinLocation[i] ]
    print(temp)
    
print("Enter denominations: ")
coins = [int(x) for x in input().split()]
amount = int(input("Enter amount: "))
coinChangeDP1(coins, amount)

        
    