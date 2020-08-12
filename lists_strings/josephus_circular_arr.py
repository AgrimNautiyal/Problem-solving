#Complete this function
def josephus(n,k):
    #Your code here
    
    arr = [i+1 for i in range(n)]
    index = 0
    l = len(arr)
    count=0
    while(True):
        if len(arr) == 1:
            return sum(arr)
        index = (index+k-1)%len(arr)
        arr.pop(index)
        count+=1
        #print(arr)