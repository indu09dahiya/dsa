# Leaders in an array

def leaders_arr(arr):
    leader = arr[-1]
    ans = []
    ans.append(leader)
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > leader:
            leader = arr[i]
            ans.append(leader)
    print(ans)
    ans.reverse()
    print(ans)
        
arr= [-3, 4, 5, 1, -4, -5]
leaders_arr(arr)
