#Dutch Flag algorithm

def sortZeroOneTwo(arr):
    
    #initialize pointers
    low,mid,high = 0,0,len(arr)-1
    
    """Looping through the array and swapping the elements 
    based on the value of arr"""
    
    while mid < high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid +=1
            low +=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
    return(arr)

arr = [1, 0, 2, 1, 0, 0, 1, 2, 1, 0]
sortZeroOneTwo(arr)
