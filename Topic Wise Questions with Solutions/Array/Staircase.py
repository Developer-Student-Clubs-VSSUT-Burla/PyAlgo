'''
A staircase of base and height both equal to n ,is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
'''
# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for j in range(n):                 
            if j>=n-i-1:          # print "#" where j>n-i-1 otherwise space will be printed
                print("#",end="")
            else:
                print(" ",end="")
        print()                   # transfer the cursor to the next line
if __name__ == '__main__':
    n = int(input())
    staircase(n)
'''
Ex:-  n=4
   #
  ##
 ###
####  
'''
