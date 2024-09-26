#The Interpolation search algorithm is an algorithm which is used for searching a given target value in a sorted array.
#Time complexity: O(log2(log2n))
#Space complexity:O(1)

import array as arr

#Function definition
def interpolationsearch(arr,arr_size,search):
    low=0
    high=arr_size-1
    while(low<=high and search<=arr[high] and search>=arr[low]):
        if low==high:
            if arr[low]==search:
                return low
        p=low+(((high-low)//(arr[high]-arr[low]))*(search-arr[low]))

        if arr[p]==search:
            return p
        elif arr[p]<search:
            low=p+1
        else:
            high=p-1

if __name__=="__main__":
    n=int(input("Enter the size of the array "))
    #Create an empty array
    a=arr.array('i',[])
    for i in range(n):
        a.append(int(input()))
    search=int(input("Enter the element that you want to find:"))

    #Function call
    int x= interpolationsearch(a,n,search)
    if x!=-1:
        print("The element is present at the index:",x)
    else:
        print("The element is not present in the array.")
