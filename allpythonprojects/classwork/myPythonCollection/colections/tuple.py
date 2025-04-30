class Tuple:
    def __init__(self, *values):
      self.item = tuple(values)

    def get(self, index):
        if 0 <= index < len(self.item):
            return self.item[index]
        raise IndexError("Index out of range!")

    def length(self):
        return len(self.item)

    def add(self, value):
        return Tuple(*self.item, value)

    def remove(self, value):
        if value not in self.item:
            print("Value not found!")
            return self
        new_data = list(self.item)
        new_data.remove(value)
        return Tuple(*new_data)

    def to_tuple(self):
       return self.item

    def display(self):
        print("Tuple Elements:", self.item)
