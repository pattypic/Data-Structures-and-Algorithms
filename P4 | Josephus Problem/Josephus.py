#  File: Josephus.py
#  Name: Patrick Pichardo
import sys

# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data):
        new_node = Link(data)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = new_node
        self.last.next = self.first

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        if self.last.data == data:
            return self.last
        
        current = self.first
        while current != self.last:
            if current.data == data:
                return current
            else:
                current = current.next
        return None

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):

        current = self.first
        if self.first.data == data:
            deleted = self.first
            self.first = current.next
            self.last.next = self.first
            return deleted
        
        while current != self.last:
            if current.next.data == data:
                if current.next == self.last:
                    self.last = current
                deleted = current.next
                current.next = current.next.next
                return deleted
            else:
                current = current.next
        return None

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        pointer = self.find(start)
        for _ in range(step - 1):
            pointer = pointer.next
        deleted = self.delete(pointer.data)
        next_node = pointer.next.data
        return deleted, next_node

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if self.is_empty():
            return "[]"
        result = str(self.first.data)
        current = self.first.next
        while current != self.first:
            result += ", " + str(current.data)
            current = current.next
        return f'[{result}]'

# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    my_list = CircularList()
    for i in range(1, num_soldiers + 1):
        my_list.insert(i)
    return my_list

# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    while num_soldiers > 1:
        deleted, start_data = my_list.delete_after(start_data, step_count)
        print(deleted)
        num_soldiers -= 1
    print(start_data)

def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
