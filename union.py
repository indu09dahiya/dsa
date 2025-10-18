# union of 2 arrays
def union_arr(arr1, arr2):
    i =0
    j=0
    while i < len(arr1) and j < len(arr2):
        if i > 0 and arr1[i] == arr1[i-1]:
            i = i+1
        elif j > 0 and arr2[j] == arr2[j-1]:
            j = j+1
        elif arr1[i] < arr2[j]:
            print(arr1[i])
            i = i+1
        elif arr2[j] < arr1[i]:
            print(arr2[j])
            j = j+1
        else:
            print(arr1[i])
            i = i+1
            j = j+1
    while i < len(arr1):
        if i > 0 and arr1[i] !=arr1[i-1]:
            print(arr1[i])
        i = i+1
    while j < len(arr2):
        if j >0 and arr2[j] !=arr2[j-1]:
            print(arr2[j])
        j = j+1

arr1 = [2,20,20,40]
arr2 = [1, 10, 20]
union_arr(arr1, arr2)
