#question url : https://practice.geeksforgeeks.org/problems/find-missing-and-repeating/0
t = int(input())
for i in range(t):
    n = int(input())
    arr = input().split()
    actual_sum = 0
    actual_product=1
    ideal_product=1
    counter=1
    for i in range(n):
        arr[i] = int(arr[i])
        actual_sum+=arr[i]
        actual_product*=arr[i]
        ideal_product*=counter
        counter+=1
    ideal_sum = n*(n+1)//2
    #now we will form 2 equations based on sum and product
    #let y = repeating element, x = missing element
    #Actual_Sum = Ideal_Sum + y - x
    #Actual_Product = Ideal_Product*y//x
    #using above equations we will calculate y and x and return
    x = (actual_sum - ideal_sum)*((ideal_product)/(actual_product-ideal_product))
    y = x*(actual_product/ideal_product)
    
    print(int(y), int(x))
    
        
    