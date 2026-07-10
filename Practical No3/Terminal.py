#S104 Pratik Rajbhar
import time
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    # Insert at specific position
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for _ in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        new_node.next = temp.next
        temp.next = new_node

    # Delete by value
    def delete_node_by_value(self, key):
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print(Fore.YELLOW + "Value not found.")
            return

        prev.next = temp.next

    # Delete by index
    def delete_node_by_index(self, position):
        if self.head is None:
            print(Fore.YELLOW + "List is empty.")
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            return

        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                raise IndexError("Position out of bounds.")

        if temp.next is None:
            raise IndexError("Position out of bounds.")

        temp.next = temp.next.next

    # Display list
    def display_list(self):
        temp = self.head

        if temp is None:
            print(Fore.RED + "Linked List is empty.")
            return

        print(Fore.GREEN + "Linked List:")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Menu
def display_menu():
    print("\n" + Style.BRIGHT + "===== Singly Linked List Operations =====")
    print("1.", Fore.BLUE + "Insert at beginning")
    print("2.", Fore.BLUE + "Insert at end")
    print("3.", Fore.BLUE + "Insert at position")
    print("4.", Fore.BLUE + "Delete a node by value")
    print("5.", Fore.BLUE + "Delete a node by index")
    print("6.", Fore.BLUE + "Display the list")
    print("7.", Fore.RED + "Exit")


# Main Function
def main():
    linked_list = LinkedList()

    while True:
        display_menu()

        try:
            choice = int(input(Style.RESET_ALL + "Enter your choice: "))

            if choice == 1:
                data = int(input("Enter data to insert at beginning: "))
                linked_list.insert_at_beginning(data)
                print(Fore.GREEN + "Node inserted at beginning.")

            elif choice == 2:
                data = int(input("Enter data to insert at end: "))
                linked_list.insert_at_end(data)
                print(Fore.GREEN + "Node inserted at end.")

            elif choice == 3:
                data = int(input("Enter data to insert: "))
                position = int(input("Enter position to insert (0-indexed): "))
                linked_list.insert_at_position(data, position)
                print(Fore.GREEN + f"Node inserted at position {position}.")

            elif choice == 4:
                data = int(input("Enter data to delete: "))
                linked_list.delete_node_by_value(data)
                print(Fore.RED + "Delete operation completed.")

            elif choice == 5:
                position = int(input("Enter index of the node to delete: "))
                linked_list.delete_node_by_index(position)
                print(Fore.RED + f"Node at index {position} deleted.")

            elif choice == 6:
                linked_list.display_list()

            elif choice == 7:
                print("Exiting...")
                break

            else:
                print(Fore.YELLOW + "Invalid choice. Please enter a valid option.")

        except ValueError:
            print(Fore.YELLOW + "Error: Please enter a valid integer.")

        except IndexError as e:
            print(Fore.RED + f"Error: {e}")

        except Exception as e:
            print(Fore.RED + f"Unexpected Error: {e}")

        time.sleep(1)


# Run Program
if __name__ == "__main__":
    main()