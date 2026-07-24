import os
import time
from termcolor import colored, cprint


class Stack:
    def __init__(self):
        self.name_stack = []

    def push(self, name):
        self.name_stack.append(name)
        print(colored(f"'{name}' has been put into the stack.", "blue"))
        self.animate_push(name)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack!")

        name = self.name_stack.pop()
        print(colored(f"'{name}' has been popped out!", "green"))
        self.animate_pop(name)
        return name

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack!")

        return self.name_stack[-1]

    def is_empty(self):
        return len(self.name_stack) == 0

    def size(self):
        return len(self.name_stack)

    def __str__(self):
        if self.name_stack:
            return " <- ".join(reversed(self.name_stack))
        return "Stack is empty"

    def animate_push(self, name):
        for _ in range(3):
            print(colored(f"Pushing {name}...", "green"))
            time.sleep(0.2)
            self.clear_screen()

    def animate_pop(self, name):
        for _ in range(3):
            print(colored(f"Popping {name}...", "yellow"))
            time.sleep(0.2)
            self.clear_screen()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def stack_operations():
    stack = Stack()

    cprint("Welcome to the Interactive Stack Operations Program!", "cyan")
    cprint("You can perform the following operations on the stack.", "cyan")

    while True:
        print("\nCurrent Stack:", colored(str(stack), "blue"))
        print(colored("1 - Push a name", "yellow"))
        print(colored("2 - Pop a name", "yellow"))
        print(colored("3 - Peek at the top item", "yellow"))
        print(colored("4 - Check if the stack is empty", "yellow"))
        print(colored("5 - Get the size of the stack", "yellow"))
        print(colored("6 - Quit", "yellow"))

        try:
            choice = int(input(colored("Choose an operation (1-6): ", "green")))
        except ValueError:
            cprint("Invalid input. Please enter a number between 1 and 6.", "red")
            continue

        if choice == 1:
            name = input(colored("Enter a student name: ", "green"))
            stack.push(name)

        elif choice == 2:
            try:
                stack.pop()
            except IndexError as e:
                cprint(str(e), "red")

        elif choice == 3:
            try:
                cprint(f"Top item: {stack.peek()}", "blue")
            except IndexError as e:
                cprint(str(e), "red")

        elif choice == 4:
            cprint(
                "Is the stack empty? " + ("Yes" if stack.is_empty() else "No"),
                "blue",
            )

        elif choice == 5:
            cprint(f"Size of the stack: {stack.size()}", "blue")

        elif choice == 6:
            cprint("Exiting the program. Goodbye!", "cyan", attrs=["bold"])
            break
        else:
            cprint("Invalid choice. Please select a number between 1 and 6.", "red")
if __name__ == "__main__":
    stack_operations()
