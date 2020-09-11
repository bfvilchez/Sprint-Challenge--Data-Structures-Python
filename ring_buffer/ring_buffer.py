class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.container = []
        self.counter = 0

    def append(self, item):

        if len(self.container) == self.capacity and self.counter == 0:
            self.container[self.counter] = item
            self.counter += 1
     

        elif len(self.container) == self.capacity and self.counter == len(self.container) - 1:
            print(self.counter)
            self.container[self.counter] = item
            self.counter = 0
          

            

        elif len(self.container) == self.capacity and self.counter != 0:
            self.container[self.counter] = item
            self.counter += 1

        else:
            self.container.append(item)
            


    def get(self, value = 0):
        old_container = self.container
        # self.container = []
        return old_container

buffer = RingBuffer(5)
buffer.append('a')
# buffer.append('b')
# buffer.append('c')

print(buffer.get())
buffer.append('d')
print(buffer.get())
# buffer.append('e')
# print(buffer.get())
# buffer.append('f')
# print(buffer.get())
# buffer.append('g')
# print(buffer.get())