import tkinter as tk
from tkinter import messagebox
print("S104 Pratik")

class Stack:
    def __init__(self):
        self.name_stack = []

    def push(self, name):
        self.name_stack.append(name)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.name_stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.name_stack[-1]

    def is_empty(self):
        return len(self.name_stack) == 0

    def size(self):
        return len(self.name_stack)

    def __str__(self):
        if self.name_stack:
            return "\n".join(reversed(self.name_stack))
        return "Stack is Empty"


class StackGUI:
    def __init__(self, root):
        self.stack = Stack()

        self.root = root
        self.root.title("Interactive Stack Operations")
        self.root.geometry("500x500")
        self.root.configure(bg="#f4f4f4")

        title = tk.Label(
            root,
            text="Stack Operations S104 Pratik",
            font=("Arial", 18, "bold"),
            bg="#f4f4f4",
            fg="navy"
        )
        title.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12), width=25)
        self.entry.pack(pady=5)

        tk.Button(root, text="Push", width=15, bg="lightgreen",
                  command=self.push_item).pack(pady=5)

        tk.Button(root, text="Pop", width=15, bg="tomato",
                  command=self.pop_item).pack(pady=5)

        tk.Button(root, text="Peek", width=15, bg="skyblue",
                  command=self.peek_item).pack(pady=5)

        tk.Button(root, text="Is Empty?", width=15, bg="khaki",
                  command=self.check_empty).pack(pady=5)

        tk.Button(root, text="Size", width=15, bg="plum",
                  command=self.show_size).pack(pady=5)

        tk.Button(root, text="Exit", width=15, bg="gray",
                  command=root.quit).pack(pady=5)

        tk.Label(
            root,
            text="Current Stack (Top to Bottom)",
            font=("Arial", 12, "bold"),
            bg="#f4f4f4"
        ).pack(pady=10)

        self.stack_display = tk.Text(root, height=10, width=30,
                                     font=("Courier", 12))
        self.stack_display.pack()

        self.update_display()

    def update_display(self):
        self.stack_display.delete(1.0, tk.END)
        self.stack_display.insert(tk.END, str(self.stack))

    def push_item(self):
        name = self.entry.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Enter a student name.")
            return

        self.stack.push(name)
        self.entry.delete(0, tk.END)
        self.update_display()
        messagebox.showinfo("Success", f"{name} pushed into the stack.")

    def pop_item(self):
        try:
            item = self.stack.pop()
            self.update_display()
            messagebox.showinfo("Popped", f"{item} removed from the stack.")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def peek_item(self):
        try:
            item = self.stack.peek()
            messagebox.showinfo("Top Item", f"Top of Stack: {item}")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def check_empty(self):
        if self.stack.is_empty():
            messagebox.showinfo("Stack Status", "The stack is empty.")
        else:
            messagebox.showinfo("Stack Status", "The stack is NOT empty.")

    def show_size(self):
        messagebox.showinfo("Stack Size", f"Size: {self.stack.size()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StackGUI(root)
    root.mainloop()
