from tkinter import *
from tkinter import messagebox, simpledialog

print("S104 Pratik Rajbhar")

class PriorityQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.capacity

    def enqueue(self, item, priority):
        if self.is_full():
            return False

        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def ascending(self):
        return sorted(self.queue, key=lambda x: x[1])

    def descending(self):
        return sorted(self.queue, key=lambda x: x[1], reverse=True)


capacity = simpledialog.askinteger(
    "Priority Queue",
    "Enter Maximum Capacity:",
    minvalue=1
)

if capacity is None:
    exit()

pq = PriorityQueue(capacity)

root = Tk()
root.title("Priority Queue GUI")
root.geometry("600x500")

title = Label(root, text="Priority Queue", font=("Arial", 18, "bold"))
title.pack(pady=10)

display = Text(root, width=60, height=15)
display.pack(pady=10)


def refresh(data):
    display.delete(1.0, END)

    if not data:
        display.insert(END, "Priority Queue is Empty")
    else:
        for item, priority in data:
            display.insert(
                END,
                f"Item : {item}    Priority : {priority}\n"
            )


def enqueue_item():
    item = simpledialog.askstring("Enqueue", "Enter Item")

    if item is None:
        return

    priority = simpledialog.askinteger(
        "Enqueue",
        "Enter Priority"
    )

    if priority is None:
        return

    if pq.enqueue(item, priority):
        messagebox.showinfo("Success", "Item Enqueued Successfully")
        refresh(pq.queue)
    else:
        messagebox.showerror("Error", "Priority Queue is Full")


def dequeue_item():
    data = pq.dequeue()

    if data is None:
        messagebox.showerror("Error", "Priority Queue is Empty")
    else:
        messagebox.showinfo(
            "Dequeued",
            f"Item : {data[0]}\nPriority : {data[1]}"
        )
        refresh(pq.queue)


def traverse():
    refresh(pq.queue)


def check_empty():
    if pq.is_empty():
        messagebox.showinfo("Status", "Priority Queue is Empty")
    else:
        messagebox.showinfo("Status", "Priority Queue is Not Empty")


def check_full():
    if pq.is_full():
        messagebox.showinfo("Status", "Priority Queue is Full")
    else:
        messagebox.showinfo("Status", "Priority Queue is Not Full")


def ascending():
    refresh(pq.ascending())


def descending():
    refresh(pq.descending())


frame = Frame(root)
frame.pack(pady=10)

Button(frame, text="Enqueue", width=18, command=enqueue_item).grid(row=0, column=0, padx=5, pady=5)
Button(frame, text="Dequeue", width=18, command=dequeue_item).grid(row=0, column=1, padx=5, pady=5)

Button(frame, text="Traverse", width=18, command=traverse).grid(row=1, column=0, padx=5, pady=5)
Button(frame, text="Check Empty", width=18, command=check_empty).grid(row=1, column=1, padx=5, pady=5)

Button(frame, text="Check Full", width=18, command=check_full).grid(row=2, column=0, padx=5, pady=5)
Button(frame, text="Ascending Order", width=18, command=ascending).grid(row=2, column=1, padx=5, pady=5)

Button(frame, text="Descending Order", width=18, command=descending).grid(row=3, column=0, padx=5, pady=5)
Button(frame, text="Exit", width=18, command=root.destroy).grid(row=3, column=1, padx=5, pady=5)

root.mainloop()