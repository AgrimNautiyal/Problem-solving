#question url : https://practice.geeksforgeeks.org/problems/get-minimum-element-from-stack/1
class stack:
    def __init__(self):
        self.s=[]
        self.mins=[]

    def push(self,x):
        #CODE HERE
        if len(self.s) == 0:
            self.mins.append(x)
        else:
            if x <= self.mins[-1]:
                self.mins.append(x)
            elif x > self.mins[-1]:
                self.mins.insert(0, x)
        self.s.append(x)

    def pop(self):
        #CODE HERE
        try:
            
            data = self.s.pop()
        
            if data == self.mins[-1]:
                self.mins.pop()

            elif data == self.mins[0]:
                self.mins.pop(0)
            return data
        except:
            return -1 
    def getMin(self):
        #CODE HERE
        try:
            return self.mins[-1]
        except:
            return -1

