import math

# To calculate x**y(mod p)
# If x and y are very large it is very difficult to compute x ** y
# So we use modular property
# (ab)mod p = ( a(mod p) * b(mod p) )mod p
def modularExponentiation(x, y, p):
    result = 1
    x = x % p
    while(y > 0):
        
        # If y is odd
        if y & 1 == 1:
            result = (result * x) % p
        
        x = (x * x) % p
        # Divide y by 2
        y = y >> 1
    
    return result


def diophantine(a, b):
    x = a
    y = b
    
    while(x % y != 0):
        temp = y
        y = x % y
        x = temp
    
    # gcd = y
    
def extendedGCD(a , b):
    x = a
    y = b
    temp = y
    y = x % y
    x = temp
    if x % y == 0:
        
        
        

    

        