class stack:
    def __init__(self):
        self.values = []
    def push(self, x):
        self.values.append(x)
    def pop(self):
        return self.values.pop()
    
s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.values)    #output=[10, 20, 30, 40]
print(s.pop())     #output = 40
print(s.values)    #output afer pop [12,20,30]