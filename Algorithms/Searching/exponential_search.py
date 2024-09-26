#The exponential search algorithm is used to searching sorted, unbounded/infinite lists.

#Time complexity: O(1) - Best case, O(log(2 i)) - average /worst case
#Space complexity: O(1)
                  

import array as arr

#Function definition
def exponentialsearch(arr, arr_size, search):
    #Checks if the element is present in the first location
    if (arr[0]==search):
        return (0)

    #Finds the range of binary search by repeated doubling
    i=1
    while(i<n and arr[i]<=search):
        i=i*2
    return binarysearch(arr,i//2,min(i, (arr_size-1)), search)

def binarysearch(arr, l, r, search):
    if r>=1:
        mid=1+(r-1)//2

        if a[mid]==search:
            return mid

        elif arr[mid]>search:
            return(binarysearch(arr, l, mid-1, search))

    #Function call
    return binarysearch(arr,mid+1,r,search)

return -1


if __name__ == "__main__":
    #Enter the size of the array
    n=int(input("Enter the number of elements:"))
    #Create an empty array
    a=arr.array('i', [])
    print("Enter the Elements:")
    for i in range(n):
        a.append(int(input()))

    #Enter the element that you want to search
    search=int(input("Enter the elemet to find: "))
    
    #Function call
    x=exponentialsearch(a, n, search)
    if x!=-1:
        print("The element is present at the index", x)
    else:
        print("The element is not present in the array.")