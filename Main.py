class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = self
        self.next = self


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        # Write code here
        tab = self.head
        if tab is None:
            self.head = Node(data)
            self.count += 1
            return True
        else:
            while tab.next is not self.head:
                tab = tab.next
            new_node = Node(data)
            tab.next = new_node
            new_node.previous = tab
            new_node.next = self.head
            self.count += 1
            return True

    def add_at_head(self, data) -> bool:
        # Write code here
        if self.head is None:
            self.head = Node(data)
            self.count = 1
            return True
        else:
            new_node = Node(data)
            tab = self.head
        while tab.next != self.head:
            tab = tab.next
        new_node.next = self.head
        new_node.previous = tab
        tab.next = new_node
        self.head = new_node
        self.count += 1
        return True        

    def add_at_index(self, index, data) -> bool:
        # Write code here
        if (index >= self.count) or (index < 0):
            return False
        if self.head is None:
            self.count = 1
            self.head = Node(data)
            return True
        else:
            tab = self.head
            if index == 0:
                tab = tab.previous
            else:
                for tel in range(index - 1):
                    tab = tab.next
            tab.next.previous = Node(data)
            tab.next.previous.next, tab.next.previous.previous = tab.next, tab
            tab.next = tab.next.previous
            if index == 0:
                self.head = self.head.previous
            self.count += 1
            return True        

    def get(self, index) -> int:
        # Write code here
        if (index >= self.count) or (index < 0):
            return -1
        if self.head is None:
            return None
        else:
            tab = self.head
            for tel in range(index):
                tab = tab.next
            return tab.data        

    def delete_at_index(self, index) -> bool:
        # Write code here
        if (index >= self.count) | (index < 0):
            return False
        if self.count == 1:
            self.head = None
            self.count -= 1
            return True

        main = self.head
        for tel in range(index):
            main = main.next

        if main is self.head:
            self.head = self.head.next

        main.previous.next, main.next.previous = main.next, main.previous
        self.count -= 1
        return True        

    def get_previous_next(self, index) -> list:
        # Write code here
        if (index >= self.count) or (index < 0) or self.head is None:
            return [-1]
        else:
            if self.count == 1:
                return [self.head.previous.data, self.head.next.data]
            else:
                counter = 0
                tab = self.head
                while counter < index:
                    tab = tab.next
                    counter += 1
                return [tab.previous.data, tab.next.data]        


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
