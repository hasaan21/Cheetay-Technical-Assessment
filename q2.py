def equillibriumPoint(arr, n):
    for i in range(n):
        # checking if sum before index equals to sum after index 
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i + 1

    # returning -1, if no equillibrium point        
    return -1        

arr = [1,3,5,4]
n = len(arr)
print(equillibriumPoint(arr,n))