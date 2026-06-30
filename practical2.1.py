import tkinter as tk
from tkinter import messagebox

stack = []

# Push
def push():
    item = entry.get()

    if item == "":
        messagebox.showwarning("Warning", "Enter a value")
        return

    stack.append(item)
    entry.delete(0, tk.END)
    display()

# Pop
def pop():
    if len(stack) == 0:
        messagebox.showerror("Error", "Stack Underflow")
    else:
        messagebox.showinfo("Deleted", stack.pop())
        display()

# Peek
def peek():
    if len(stack) == 0:
        messagebox.showinfo("Stack", "Stack Empty")
    else:
        messagebox.showinfo("Top Element", stack[-1])

# Display
def display():
    listbox.delete(0, tk.END)

    for item in reversed(stack):
        listbox.insert(tk.END, item)

# Delimiter Matching
def delimiter():
    expression = entry.get()

    temp = []
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in expression:

        if ch in "([{":
            temp.append(ch)

        elif ch in ")]}":

            if not temp or temp.pop() != pairs[ch]:
                messagebox.showinfo("Result", "Not Balanced")
                return

    if len(temp) == 0:
        messagebox.showinfo("Result", "Balanced")
    else:
        messagebox.showinfo("Result", "Not Balanced")

# Prefix to Postfix
def prefix_postfix():

    prefix = entry.get()

    temp = []

    for ch in reversed(prefix):

        if ch.isalnum():
            temp.append(ch)

        else:
            op1 = temp.pop()
            op2 = temp.pop()

            temp.append(op1 + op2 + ch)

    messagebox.showinfo("Postfix", temp[-1])

# Evaluate Postfix
def evaluate():

    postfix = entry.get()

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

    messagebox.showinfo("Result", temp.pop())

# Window
root = tk.Tk()

root.title("Stack Implementation")
root.geometry("350x500")

tk.Label(root,text="Enter Value / Expression",font=("Arial",12)).pack()

entry = tk.Entry(root,width=30)
entry.pack(pady=5)

tk.Button(root,text="Push",command=push).pack(fill="x")
tk.Button(root,text="Pop",command=pop).pack(fill="x")
tk.Button(root,text="Peek",command=peek).pack(fill="x")
tk.Button(root,text="Delimiter Matching",command=delimiter).pack(fill="x")
tk.Button(root,text="Prefix to Postfix",command=prefix_postfix).pack(fill="x")
tk.Button(root,text="Evaluate Postfix",command=evaluate).pack(fill="x")

listbox = tk.Listbox(root,height=12)
listbox.pack(fill="both",pady=10)

root.mainloop()
