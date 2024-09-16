'''
Problem:
Given two strings st1 and st2 we have to convert st1 to st2 using certain 
operations : 
1) Insert
2) Remove
3) Replace
You are asked to find the minimum operations required to convert st1 to st2
'''
def solve(dp,s1,s2,i,j):# Function to find the min opr required
	if i==len(s1) and j==len(s2):
		return 0
	if i>=len(s1):#If s1 have no element left to search then return the remaining elements in s2
		return len(s2)-j
	elif j>=len(s2):#If s2 have no element left to search then return the remaining elements in s1
		return len(s1)-i
	if s1[i]==s2[j]:# If s1[i]==s2[j] then increament the pointer by 1 on both of the strings
		return solve(dp,s1,s2,i+1,j+1)
	if dp[i][j]!=-1:# If dp[i][j] is not -1 then return the value of dp[i][j]
		return dp[i][j]
	else:
		a=1+solve(dp,s1,s2,i,j+1)#Insert
		b=1+solve(dp,s1,s2,i+1,j)#Remove
		c=1+solve(dp,s1,s2,i+1,j+1)#Replace
		dp[i][j]=min(min(a,b),c)#This will find the min opr required
	return dp[i][j]
#main
if __name__=="__main__":
	s1=input("Enter the first string : ")# Enter the first number
	s2=input("Enter the second string : ")# Enter the second number
	dp=[[-1 for i in range(len(s2))] for j in range(len(s1))]# Initialize each value on dp to -1
	print("Min operations required :  ",solve(dp,s1,s2,0,0))#Print the minimum operations
'''
Input:
Enter the first string : geek
Enter the second string : gesek
Output:
Min operations required :  1

Time Complexity : O(length(st1)*length(st2))
Space Complexity : O(length(st1)*length(st2))
'''
