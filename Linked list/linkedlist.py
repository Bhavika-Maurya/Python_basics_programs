class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # def insert_beginning(self, data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head.prev = new_node
    #         self.head = new_node

    # def delete(self, data):
    #     current = self.head
    #     while current:
    #         if current.data == data:
    #             if current.prev:
    #                 current.prev.next = current.next
    #             else:
    #                 self.head = current.next

    #             if current.next:
    #                 current.next.prev = current.prev
    #             else:
    #                 self.tail = current.prev

    #             return
    #         current = current.next

    # def display(self):
    #     current = self.head
    #     while current:
    #         print(current.data, end=" <-> ")
    #         current = current.next
    #     print("None")

def main():
    linked_list = DoublyLinkedList()

    while True:
        print("\nMenu:")
        print("1. Insert at the end")
        print("2. Insert at the beginning")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            linked_list.insert_end(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            linked_list.insert_beginning(data)
        elif choice == 3:
            data = int(input("Enter data to delete: "))
            linked_list.delete(data)
        elif choice == 4:
            linked_list.display()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
