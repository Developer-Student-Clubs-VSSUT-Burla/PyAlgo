'''
	    Bilinear search is a searching algorithm where the program searches for an element
	    from both ends. It is an improved version of linear search.
	'''
	

	

	def bilinear_search(list, x):
	    size = len(list)
	    i = 0
	    j = size-1
	    flag=0
	

	    while i < j:
	        if list[i] == x or list[j] == x:
	            flag=1
	            break
	        else:
	            i = i+1
	            j = j-1
	            
	    if flag == 1:
	        return True
	    else:
	        return False
	

	if __name__ == "__main__":
	    list1 = list(map(int,input("Enter the numbers : ").strip().split(',')))[:10000000]
	

	    x = int(input("Enter the element to check : "))
	

	    if bilinear_search(list1, x):
	        print("Element Found")
	    else:
	        print("Element not Found")
	

	

	'''
	   Input -
	            Enter the numbers: 22, 32, 42, 52, 62, 72
	            Enter the element to check: 52
	   Output - 
	            Element Found
	
	
	   Input -
	            Enter the numbers: 22, 32, 42, 52, 62, 72
	            Enter the element to check: 82
	   Output - 
	            Element not Found
	'''
	

