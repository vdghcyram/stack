class Stack:
   _stack = []

   def push_item(self, item):
       self._stack = [item] + self._stack

   def pop_item(self):
       tmp = self._stack[0]
       self._stack.remove(self._stack[0])
       return tmp

   def get_stack(self):
       return self._stack

   def empty(self):
       if len(self._stack)==0:
           return True

my_stack = Stack()
_str = input()
for l in _str:
    if l == '(':
        my_stack.push_item()
    elif l == ')':
        if my_stack.emply():
            print('ошибка')
            exit()
        else:
            my_stack.pop_item()
if my_stack.emply():
    print('верно')
else:
    print('ошибка')