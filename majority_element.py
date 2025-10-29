#Find majority element - an element is called majority element if its occurrence is greater than n/2 where n is size of the array

def majority_elem(arr):
    size = int(len(arr)//2)
    hash_list = [0]*(int(max(arr))+1)
   
    for i in arr:
        hash_list[i] +=1
           
    if max(hash_list) > size:
        print("majority")
    else:
        print("no majority")

arr = [1,2,2,2,5,7,2,4,2,3,2]
majority_elem(arr)
