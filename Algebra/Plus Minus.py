'''
A python program to calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''
# Complete the plusMinus function below.
def plusMinus(arr):
    l=len(arr)
    cn=0  #counter used to count negative numbers
    cp=0  #counter used to count positive numbers
    cz=0  #counter used to count zeroes
    for i in arr:
        if i<0:    # check for negative numbers
            cn+=1
        elif i>0:    # check for positive numbers
            cp+=1
        else:
            cz+=1

    p=cp/l
    n=cn/l
    z=cz/l
    print(format(p,".6f"))  #format() is used to print value upto 6 decimal places
    print(format(n,".6f"))  
    print(format(z,".6f"))

'''
Sample Input/ Output:
Input:
n=5
arr = [1, 1, 0, -1, -1]
----------------------
Output:
0.400000
0.400000
0.200000
'''
