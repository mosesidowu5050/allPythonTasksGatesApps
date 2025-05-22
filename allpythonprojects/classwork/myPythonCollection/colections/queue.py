class MyQueueClass:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        if self.queue == 0:
            return True
        else:
            return False

    def add_element_to_queue(self, value):
        if self.is_empty():
            return "Queue is empty"
        else:
            self.queue.append(value)
            self.size += 1

    def remove_an_element(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            self.size -= 1
            return self.queue.pop(0)

    def get_front_element(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[0]

    def get_back_element(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[-1]

    def length_of_queue(self):
        if not self.is_empty():
            return len(self.queue)
        else:
            return 0

    def display_queue(self):
        if self.is_empty():
            return "No element in the Queue"
        else:
            print(self.queue)

