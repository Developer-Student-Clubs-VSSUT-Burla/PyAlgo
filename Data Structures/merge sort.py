""" Merge sort is a divide and conquer algorithm that works on dividing
the array into 2 parts, sorting each part and then merging them to form
the final sorted array. Time Complexity=O(nlogn) """

def merge(a,q):
    L=a[:q]
    R=a[q:]
    i=j=k=0
    while i<len(L) and j<len(R):
        if(L[i]<R[j]):
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1

    while i<len(L):
        a[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        a[k]=R[j]
        j+=1
        k+=1
    return a


def mergeSort(a, p, r):
    if p>=r:
        return
    q=(p+r)//2
    mergeSort(a,p,q)
    mergeSort(a,q+1,r)
    a=merge(a,q)


array=list(map(int, input("Enter the array- ").split()))
mergeSort(array, 0, len(array))
print("The sorted array is-{}".format(array))
