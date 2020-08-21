#question url : https://practice.geeksforgeeks.org/problems/implement-stack-using-array/1
class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Adds element to the Stack
    def push(self,data):
        #add code here
        self.arr.append(data)
    
    #Removes element from the stack
    def pop(self):
        #add code here
        try:
            return self.arr.pop()
        except:
            return -1 
        