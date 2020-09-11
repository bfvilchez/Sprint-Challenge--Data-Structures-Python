class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        self.duplicates = {}

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()

    def duplicate_values(self,values = {}):

        name_set = set(self.storage).difference()
        self.duplicates = name_set.intersection(values)
        return self.duplicates


    def print_values(self):
        print(self.duplicates)




import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
stack = Stack()
for name_1 in names_1:
    stack.push(name_1)

duplicates = stack.duplicate_values(names_2)

# name_1Set = names_1
# name_2Set = names_2

# for name_1 in name_1Set:
#     for name_2 in name_2Set:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

