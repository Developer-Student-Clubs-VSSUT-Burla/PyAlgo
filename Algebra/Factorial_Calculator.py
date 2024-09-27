'''
Aim: Compute factorial of the entered number.

'''

def factorial(n):
    s = 1                    
    for i in range(1,n+1):   # calculating factorial in this step
        s = s*i              # multiplying all integers from 1 to the entered number
    print(s)
    
n = int(input().strip())     # getting the input
factorial(n)                 # calling 'factorial' function to compute the factorial and display the output

'''
Sample Test Case:
Input: 
5
Output: 
120
Explaination:
5! = 1*2*3*4*5 = 120

'''