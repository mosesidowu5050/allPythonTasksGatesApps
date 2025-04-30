class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def peek(self):
        if not self.is_empty():
            return self.stack[len(self.stack) - 1]
        else:
            return "Stack is empty"

    def pop(self):
        return self.stack.pop()

    def clear(self):
        self.stack = []
        self.size = 0

    def remove(self,value):
        if not self.is_empty():
            return self.stack.remove(value)
        else:
            return "No element to remove, stack is empty"

    def is_empty(self):
        return self.stack == []

    def set_element(self, index, value):
        if 0 <= index < self.size:
            self.stack[index] = value
            self.size += 1
        else:
            print("Index out of range!")

    def length(self):
        if not self.is_empty():
            return len(self.stack)
        else:
            return "Stack is empty"

    def check_index(self, index):
        if 0 <= index < self.size:
            return self.stack[index]
        else:
            print("Index out of range!")


