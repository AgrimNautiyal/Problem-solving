def matrixify(arr, rows, columns):
    res=[]
    idx=0
    for i in range(rows):
        res.append(arr[idx:idx+columns])
        idx+=columns
    return res
    
t=int(input())
for i in range(t):
    inp = list(map(int, input().split()))
    row = inp[0]
    col = inp[1]
    
    ele = list(map(int, input().split()))
    
    m = matrixify(ele, row, col)
    #m contains our 2D matrix
    top = 0
    bottom= row-1
    left = 0 
    right = col-1
    d = 0 #direction
    res=[]

    while(top<=bottom and left<=right):
        if d == 0:
            #move left to right
            for i in range(left, right+1):
                res.append(m[top][i])
            top+=1
        elif d == 1:
            #move top to bottom
            for i in range(top, bottom+1):
                res.append(m[i][right])
            right-=1
        elif d == 2:
            #move right to left
            for i in range(right, left-1, -1):
                res.append(m[bottom][i])
            bottom-=1
        elif d == 3:
            #move bottom to top
            for i in range(bottom, top-1, -1):
                res.append(m[i][left])
            left+=1
        d = (d+1)%4
    
    print(' '.join(map(str, res)))