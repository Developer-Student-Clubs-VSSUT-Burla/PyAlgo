# Python Program to print n terms
# of Newman-Conway Sequence

def sequence(n):

	# Function to find
	# the n-th element
	# Declare array to store sequence
	f = [0, 1, 1]

	print(f[1], end=" "),
	print(f[2], end=" "),
	for i in range(3,n+1):
		f.append( f[f[i - 1]] + f[i - f[i - 1]])
		print(f[i], end=" "),
		
# driver code
n = 13
sequence(n)


