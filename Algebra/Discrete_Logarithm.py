# discrete logarithm
# a^k ≡ b(mod m)a

import math
from sympy.ntheory.factor_ import totient 
  
def DiscreteLogarithm(a,b,m):
    b = b % m
    for i in range (totient(m)):
        x = math.pow(a,i) % m
        if (x == b):
            return i
    return -1

print("Enter value for:")
# sample values a=45, b=78, m=89, k=3
a = int(input("a:"))   
b = int(input("b:"))   
m = int(input("c:"))   
print(DiscreteLogarithm(a,b,m))

