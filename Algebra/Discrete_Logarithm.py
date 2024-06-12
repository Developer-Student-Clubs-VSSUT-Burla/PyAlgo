# discrete logarithm
# If a,b,m are given then among the numbers 0,1,2....,phi(n) (phi(n) is the totient function)
# exactly one number 'k' such that a^k ≡ b(mod m), where b and m are relatively prime.
# Then 'k' is called the discrete logarithm of b 

import math
from sympy.ntheory.factor_ import totient 

# Function DiscreteLogarithm() checks if 'k' exists for the given values of a,b,m 
# -1 is returned if such value doesn't exist 
def DiscreteLogarithm(a,b,m):
    b = b % m
    for i in range (totient(m)):
        x = math.pow(a,i) % m
        if (x == b):
            return i
    return -1

print("Enter value for:")
a = int(input("a:"))   
b = int(input("b:"))   
m = int(input("m:"))   
print(DiscreteLogarithm(a,b,m))

''' Sample input:  a=45, b=78, m=89    
    output - value of 'k' that satisfies a^k ≡ b(mod m)
           =  3 '''
