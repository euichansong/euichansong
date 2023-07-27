import sys
class Save:
    
    def __init__(self):
        self.stack = []

    def push(self, num) :
        self.num = num
        return self.stack.append(num)
        
    def pop(self):
        if len(self.stack) != 0:
            a = self.stack.pop()
            return print(int(a))
        else:
            return print(-1)
    def size(self):
        return print(len(self.stack))
        
    def empty(self):
        if len(self.stack) != 0:
            return print(0)
        else:
            return print(1)
        
    def top(self):
        if len(self.stack) == 0:
            return print(-1)
        else:
            return print(self.stack[-1])
        
n = int(sys.stdin.readline().rstrip())
save = Save()
for i in range(n):
    word2 = sys.stdin.readline().rsplit()
    word = word2[0]
    if word == 'push':
        num = word2[1]
        save.push(num)
    elif word == 'top':
        save.top()
    elif word == 'pop':
        save.pop()
    elif word == 'size':
        save.size()
    elif word == 'empty':
        save.empty()

# stack = []
# class Save:
            
#     def push(self, n) :
#         self.num = n
#         return stack.append(num)

#     def pop(self):
#         a = stack.pop()
#         return print(a)

#     def size(self):
#         return print(len(stack))
    
#     def empty(self):
#         if len(stack) == 1:
#             return print(0)
#         else:
#             return print(1)
    
#     def top(self):
#         if len(stack) == 0:
#             return print(-1)
#         else:
#             return print(stack[0])

# n = int(sys.stdin.readline())
# for i in range(n):
#     word2 = sys.stdin.readline().split()
#     word = word2[0]
#     if word == 'push':
#         num = word2[1]
#         self.push(num)
#     elif word == 'top':
#         self.top()
#     elif word == 'pop':
#         self.pop()
#     elif word == 'size':
#         self.size()
#     elif word == 'empty':
#         self.empty()

