# count inversions in an array
"""
A pair arr[i], arr[j] forms an invesrion when i <j and arr[i] > arr[j]

"""
def count_invserion(arr):
    for i in range(0, len(arr)):
        ele = arr[i]
        for j in range(i+1, len(arr)):
            if ele > arr[j]:
                print(ele, arr[j])

#arr = [2,4, 1,3,5]
arr = [40, 30, 20,10]
count_invserion(arr)
