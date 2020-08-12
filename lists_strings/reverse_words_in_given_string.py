#question url : https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

t= int(input())
for i in range(t):
    #simple logic : split string based on '.', reverse list, then join list with '.' as separator into a string 
    print('.'.join(map(str, input().split('.')[::-1])))
    
    