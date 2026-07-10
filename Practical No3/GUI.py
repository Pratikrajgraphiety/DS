# S104 Pratik Rajbhar

import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_at_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def insert_at_position(self, data, pos):
        new = Node(data)

        if pos == 0:
            new.next = self.head
            self.head = new
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                raise IndexError("Position out of bounds.")
            temp = temp.next

        if temp is None:
            raise IndexError("Position out of bounds.")

        new.next = temp.next
        temp.next = new

    def delete_by_value(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return True

        prev = None

        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return False

        prev.next = temp.next
        return True

    def delete_by_index(self, pos):
        if self.head is None:
            raise IndexError("List is empty.")

        temp = self.head

        if pos == 0:
            self.head = temp.next
            return

        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                raise IndexError("Position out of bounds.")

        if temp.next is None:
            raise IndexError("Position out of bounds.")

        temp.next = temp.next.next

    def get_list(self):
        result = ""

        temp = self.head

        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next

        result += "None"
        return result

linked_list = LinkedList()

def refresh():
    output.delete("1.0", tk.END)
    output.insert(tk.END, linked_list.get_list())

def get_data():
    return int(data_entry.get())

def get_position():
    return int(position_entry.get())

def insert_beginning():
    try:
        linked_list.insert_at_beginning(get_data())
        refresh()
        messagebox.showinfo("Success", "Node inserted at beginning.")
    except:
        messagebox.showerror("Error", "Enter valid data.")

def insert_end():
    try:
        linked_list.insert_at_end(get_data())
        refresh()
        messagebox.showinfo("Success", "Node inserted at end.")
    except:
        messagebox.showerror("Error", "Enter valid data.")

def insert_position():
    try:
        linked_list.insert_at_position(get_data(), get_position())
        refresh()
        messagebox.showinfo("Success", "Node inserted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_value():
    try:
        if linked_list.delete_by_value(get_data()):
            refresh()
            messagebox.showinfo("Success", "Node deleted.")
        else:
            messagebox.showwarning("Not Found", "Value not found.")
    except:
        messagebox.showerror("Error", "Enter valid value.")

def delete_index():
    try:
        linked_list.delete_by_index(get_position())
        refresh()
        messagebox.showinfo("Success", "Node deleted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Singly Linked List")
root.geometry("550x500")
root.resizable(False, False)

title = tk.Label(root,
                 text="Singly Linked List Operations",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Data").grid(row=0, column=0, padx=5, pady=5)
data_entry = tk.Entry(frame)
data_entry.grid(row=0, column=1)

tk.Label(frame, text="Position").grid(row=1, column=0, padx=5, pady=5)
position_entry = tk.Entry(frame)
position_entry.grid(row=1, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame,
          text="Insert Beginning",
          bg="Green",
          width=18,
          command=insert_beginning).grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame,
          text="Insert End",
          bg="Blue",
          width=18,
          command=insert_end).grid(row=0, column=1, padx=5, pady=5)

tk.Button(btn_frame,
          text="Insert Position",
          bg="Yellow",
          width=18,
          command=insert_position).grid(row=1, column=0, padx=5, pady=5)

tk.Button(btn_frame,
          text="Delete by Value",
          bg="Orange",
          width=18,
          command=delete_value).grid(row=1, column=1, padx=5, pady=5)

tk.Button(btn_frame,
          text="Delete by Index",
          bg="Pink",
          width=18,
          command=delete_index).grid(row=2, column=0, padx=5, pady=5)

tk.Button(btn_frame,
          text="Display List",
          width=18,
          bg="Grey",
          command=refresh).grid(row=2, column=1, padx=5, pady=5)

tk.Button(root,
          text="Exit",
          width=20,
          bg="red",
          fg="Blue",
          command=root.destroy).pack(pady=10)

output = tk.Text(root,
                 width=60,
                 height=10,
                 font=("Consolas", 12))
output.pack(pady=10)

refresh()

root.mainloop()
