def duplicates(arr, n): 
	# code here
    for i in range(0, n):
        arr[arr[i]%n] = arr[arr[i]%n] + n
    flag = 0
    res=[]
    for i in range(0, n):
        if arr[i]>=2*n:
            res.append(i)
	   
    if len(res) == 0:
        return [-1]
    else:
        return sorted(res)

