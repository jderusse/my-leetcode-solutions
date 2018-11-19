class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, data):
        self.elements.append(data)
    
    def pop(self):
        return self.elements.pop()


class Solution:
    def reverse(self, x):
        stringyfied = str(x)
        is_negative = False
        
        if stringyfied[0] == "-":
            is_negative = True
        
        stringyfied = stringyfied.replace("-", "")
        
        intList = map(int, stringyfied)
        integerStack = Stack()
        
        for integer in intList:
            integerStack.push(integer)
            
        reversed_list = []
        
        while len(integerStack.elements) > 0:
            reversed_list.append(integerStack.pop())
        
        reversetIntStr = ''.join(str(i) for i in reversed_list)
        if is_negative:
            reversetIntStr = '-%s' %(reversetIntStr)
        
        return int(reversetIntStr)