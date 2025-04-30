class Lists:
    def __init__(self):
        self.item = []
        self.size = 0

    def append_element(self, value):
        self.item += [value]
        self.size += 1

    def get(self, index):
        if 0 <= index < self.size:
            return self.item[index]
        print("Index out of range!")
        return None

    def set_element(self, index, value):
        if 0 <= index < self.size:
            self.item[index] = value
        else:
            print("Index out of range!")

    def length(self):
        if self.size == 0:
            return 0
        else:
            return self.size

    def clear(self):
        self.size = 0
        self.item = []

    def reverse(self):
        if self.size == 0:
            return []
        else:
            return self.item[::-1]

    def display(self):
        print("Elements in List:", self.item)
