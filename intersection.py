#intersection of 2 sorted arrays

def intersection_arr(arr1, arr2):
    i = 0    
    j = 0
    empty_list = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i=i+1
        elif arr1[i] > arr2[j]:
            j=j+1
        else:
            empty_list.append(arr1[i])
            i = i+1
            j = j+1
            
    print(empty_list)
    
    
    
    
arr1 = [1,5,5,10,10,15,20, 24]
arr2 = [3,5,7,10,15, 20]
intersection_arr(arr1, arr2)
