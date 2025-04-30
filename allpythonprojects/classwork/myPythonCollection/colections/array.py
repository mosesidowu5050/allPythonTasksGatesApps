class ArrayClass:

    def __init__(self, capacity=4):
        self.array = [0] * capacity
        self.actual_elements = 0
        self.capacity = capacity

    def append(self, value):
        if self.actual_elements == self.capacity:
            self.resize()
        self.array[self.actual_elements] = value
        self.actual_elements += 1

    def get(self, index):
        if 0 <= index < self.actual_elements:
            return self.array[index]
        print("Index out of range!")
        return 0

    def set(self, index, value):
        if 0 <= index < self.actual_elements:
            self.array[index] = value
        else:
            print("Index out of range!")

    def length(self):
        return self.actual_elements

    def resize(self):
        new_capacity = self.capacity * 2
        new_data = [0] * new_capacity
        for item in range(self.actual_elements):
            new_data[item] = self.array[item]
        self.array = new_data
        self.capacity = new_capacity

    def remove(self, index):
        if index < 0 or index >= self.actual_elements:
            print("Index out of range!")
            return
        for item in range(index, self.actual_elements - 1):
            self.array[item] = self.array[item + 1]
        self.array[self.actual_elements - 1] = 0
        self.actual_elements -= 1

    def display(self):
        print("Elements in the Array:", self.array[:self.actual_elements])

    def display_all_elements(self):
        print("Elements in the Array:", self.array)


