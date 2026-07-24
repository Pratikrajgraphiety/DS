import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(Fore.GREEN + "Inserted " + str(data) + " into empty list.")
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        print(Fore.GREEN + "Inserted " + str(data) + " at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(Fore.GREEN + "Inserted " + str(data) + " into empty list.")
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp
        print(Fore.GREEN + "Inserted " + str(data) + " at the end.")

    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        if position < 1:
            print(Fore.RED + "Position must be 1 or greater.")
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        temp = self.head
        count = 1
        
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print(Fore.RED + "Position out of bounds.")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node
            
        temp.next = new_node
        print(Fore.GREEN + "Inserted " + str(data) + " at position " + str(position) + ".")

    def delete_by_value(self, key):
        if self.head is None:
            print(Fore.RED + "List is empty. Nothing to delete.")
            return

        temp = self.head

        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(Fore.YELLOW + "Deleted node with value " + str(key) + ".")
            return

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print(Fore.RED + "Node with value " + str(key) + " not found.")
            return

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

        print(Fore.YELLOW + "Deleted node with value " + str(key) + ".")

    def traverse_list(self):
        if self.head is None:
            print(Fore.CYAN + "List is empty: None")
            return

        print(Fore.MAGENTA + "\nList Traversal:")
        temp = self.head
        output = []
        while temp:
            node_str = Fore.BLACK + Back.WHITE + " " + str(temp.data) + " " + Style.RESET_ALL
            output.append(node_str)
            temp = temp.next
        
        pointer = " <-> "
        print(pointer.join(output) + " -> None")


def main():
    dll = DoublyLinkedList()
    
    while True:
        print("\n")
        print(f"{Back.BLUE}{Fore.WHITE}  Linked List Operations Menu  ")
        print(f"{Fore.CYAN}1. {Fore.WHITE}Insert at Beginning")
        print(f"{Fore.CYAN}2. {Fore.WHITE}Insert at End")
        print(f"{Fore.CYAN}3. {Fore.WHITE}Insert at Position")
        print(f"{Fore.CYAN}4. {Fore.WHITE}Delete by Value")
        print(f"{Fore.CYAN}5. {Fore.WHITE}Traverse List")
        print(f"{Fore.CYAN}6. {Fore.WHITE}Exit")
        print("\n")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            val = input("Enter value to insert at beginning: ")
            dll.insert_at_beginning(val)
            dll.traverse_list()
        elif choice == '2':
            val = input("Enter value to insert at end: ")
            dll.insert_at_end(val)
            dll.traverse_list()
        elif choice == '3':
            val = input("Enter value to insert: ")
            pos = int(input("Enter position (starting from 1): "))
            dll.insert_at_position(val, pos)
            dll.traverse_list()
        elif choice == '4':
            val = input("Enter value to delete: ")
            dll.delete_by_value(val)
            dll.traverse_list()
        elif choice == '5':
            dll.traverse_list()
        elif choice == '6':
            print(Fore.GREEN + "Exiting the program.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    main()
