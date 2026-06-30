#S104 Pratik Rajbhar

stack = []
undo_stack = []


def push():
    item = input("Enter element: ")
    stack.append(item)
    undo_stack.append(("pop",))
    print(item, "inserted successfully.")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        item = stack.pop()
        undo_stack.append(("push", item))
        print("Deleted Element:", item)

def peek():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Top Element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("\nStack Elements (Top to Bottom)")
        for item in reversed(stack):
            print(item)

# Delimiter Matching

def delimiter_matching():
    expression = input("Enter Expression: ")

    temp = []
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in expression:
        if ch in "([{":
            temp.append(ch)
        elif ch in ")]}":
            if not temp or temp.pop() != pairs[ch]:
                print("Not Balanced")
                return

    if len(temp) == 0:
        print("Balanced Expression")
    else:
        print("Not Balanced")

# Undo

def undo():
    if len(undo_stack) == 0:
        print("Nothing to Undo")
        return

    action = undo_stack.pop()

    if action[0] == "pop":
        if stack:
            stack.pop()

    elif action[0] == "push":
        stack.append(action[1])

    print("Undo Successful")

# Prefix to Postfix

def prefix_to_postfix():
    prefix = input("Enter Prefix Expression: ")

    temp = []

    for ch in reversed(prefix):
        if ch.isalnum():
            temp.append(ch)
        else:
            op1 = temp.pop()
            op2 = temp.pop()
            temp.append(op1 + op2 + ch)

    print("Postfix Expression:", temp[-1])

# Evaluate Postfix

def evaluate_postfix():
    postfix = input("Enter Postfix Expression: ")

    temp = []

    for ch in postfix:

        if ch.isdigit():
            temp.append(int(ch))

        else:
            b = temp.pop()
            a = temp.pop()

            if ch == '+':
                temp.append(a+b)

            elif ch == '-':
                temp.append(a-b)

            elif ch == '*':
                temp.append(a*b)

            elif ch == '/':
                temp.append(a//b)

            elif ch == '^':
                temp.append(a**b)

    print("Result =", temp.pop())

# Menu

while True:

    print("\n========== STACK MENU ==========")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Delimiter Matching")
    print("6. Undo")
    print("7. Prefix to Postfix")
    print("8. Evaluate Postfix")
    print("9. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        push()

    elif choice == '2':
        pop()

    elif choice == '3':
        peek()

    elif choice == '4':
        display()

    elif choice == '5':
        delimiter_matching()

    elif choice == '6':
        undo()

    elif choice == '7':
        prefix_to_postfix()

    elif choice == '8':
        evaluate_postfix()

    elif choice == '9':
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
