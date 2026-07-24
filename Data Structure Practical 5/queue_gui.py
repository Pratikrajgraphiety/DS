import tkinter as tk
from tkinter import ttk, messagebox


class QueueGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Operations BY S104 Pratik")
        self.root.geometry("700x500")
        self.root.configure(bg="pink")

        self.queue = []

        # ===== Title =====
        title = tk.Label(
            root,
            text="QUEUE GUI S104",
            font=("Arial", 22, "bold"),
            bg="blue",
            fg="white"
        )
        title.pack(pady=15)

        # ===== Max Size =====
        frame1 = tk.Frame(root, bg="#2C3E50")
        frame1.pack()

        tk.Label(
            frame1,
            text="Maximum Queue Size:",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="white"
        ).grid(row=0, column=0, padx=5)

        self.max_size_entry = ttk.Entry(frame1, width=10)
        self.max_size_entry.grid(row=0, column=1)
        self.max_size_entry.insert(0, "5")

        # ===== Item Entry =====
        frame2 = tk.Frame(root, bg="#2C3E50")
        frame2.pack(pady=20)

        tk.Label(
            frame2,
            text="Enter Item:",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="white"
        ).grid(row=0, column=0)

        self.item_entry = ttk.Entry(frame2, width=20)
        self.item_entry.grid(row=0, column=1, padx=10)

        # ===== Buttons =====
        button_frame = tk.Frame(root, bg="#2C3E50")
        button_frame.pack()

        buttons = [
            ("Enqueue", "#27AE60", self.enqueue),
            ("Dequeue", "#E74C3C", self.dequeue),
            ("Peek", "#3498DB", self.peek),
            ("Display", "#9B59B6", self.display),
            ("Is Empty?", "#16A085", self.is_empty),
            ("Is Full?", "#F39C12", self.is_full),
            ("Clear", "#34495E", self.clear_queue)
        ]

        row = 0
        col = 0

        for text, color, cmd in buttons:
            b = tk.Button(
                button_frame,
                text=text,
                bg=color,
                fg="white",
                font=("Arial", 11, "bold"),
                width=12,
                command=cmd
            )
            b.grid(row=row, column=col, padx=8, pady=8)

            col += 1
            if col == 3:
                row += 1
                col = 0

        # ===== Queue Display =====
        tk.Label(
            root,
            text="Queue",
            font=("Arial", 15, "bold"),
            bg="#2C3E50",
            fg="white"
        ).pack()

        self.listbox = tk.Listbox(
            root,
            width=50,
            height=8,
            font=("Arial", 14),
            bg="white",
            fg="black"
        )
        self.listbox.pack(pady=10)

        # ===== Status =====
        self.status = tk.Label(
            root,
            text="Welcome!",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="yellow"
        )
        self.status.pack()

    def max_size(self):
        try:
            return int(self.max_size_entry.get())
        except:
            return 5

    def update_display(self):
        self.listbox.delete(0, tk.END)
        for i, item in enumerate(self.queue):
            self.listbox.insert(tk.END, f"{i+1}. {item}")

    def enqueue(self):
        item = self.item_entry.get()

        if item == "":
            messagebox.showwarning("Warning", "Enter an item.")
            return

        if len(self.queue) >= self.max_size():
            messagebox.showerror("Queue Full", "Queue is Full!")
            return

        self.queue.append(item)
        self.status.config(text=f"Enqueued: {item}", fg="lightgreen")
        self.item_entry.delete(0, tk.END)
        self.update_display()

    def dequeue(self):
        if not self.queue:
            messagebox.showerror("Empty", "Queue is Empty!")
            return

        item = self.queue.pop(0)
        self.status.config(text=f"Dequeued: {item}", fg="orange")
        self.update_display()

    def peek(self):
        if not self.queue:
            messagebox.showinfo("Peek", "Queue is Empty")
        else:
            messagebox.showinfo("Front Item", self.queue[0])

    def display(self):
        self.update_display()

    def is_empty(self):
        if not self.queue:
            messagebox.showinfo("Queue", "Queue is Empty")
        else:
            messagebox.showinfo("Queue", "Queue is NOT Empty")

    def is_full(self):
        if len(self.queue) == self.max_size():
            messagebox.showinfo("Queue", "Queue is Full")
        else:
            messagebox.showinfo("Queue", "Queue is NOT Full")

    def clear_queue(self):
        self.queue.clear()
        self.update_display()
        self.status.config(text="Queue Cleared", fg="red")


root = tk.Tk()
app = QueueGUI(root)
root.mainloop()
