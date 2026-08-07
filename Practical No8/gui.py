import tkinter as tk
from tkinter import ttk
import heapq

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.logs = []

    def insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        self.logs.append(f"Left Rotation on {z.key}")
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        self.logs.append(f"Right Rotation on {z.key}")
        return y

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def preorder(self, root):
        result = []

        def traverse(node):
            if node:
                result.append(str(node.key))
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return " ".join(result)


class Application:

    def __init__(self, root):

        self.root = root
        self.root.title("AVL Tree, Heap & Priority Queue")
        self.root.geometry("800x650")

        self.avl = AVLTree()
        self.avl_root = None

        self.tasks = []

        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)

        avl_tab = ttk.Frame(notebook)
        notebook.add(avl_tab, text="AVL Tree")

        ttk.Label(avl_tab, text="Enter Value").pack(pady=5)

        self.avl_entry = ttk.Entry(avl_tab)
        self.avl_entry.pack()

        ttk.Button(
            avl_tab,
            text="Insert",
            command=self.insert_avl
        ).pack(pady=5)

        self.avl_output = tk.Text(avl_tab, height=20)
        self.avl_output.pack(fill="both", expand=True)

        heap_tab = ttk.Frame(notebook)
        notebook.add(heap_tab, text="Heap")

        ttk.Label(heap_tab,
                  text="Numbers (comma separated)").pack(pady=5)

        self.heap_entry = ttk.Entry(heap_tab, width=50)
        self.heap_entry.insert(0, "9,5,6,2,3")
        self.heap_entry.pack()

        ttk.Button(
            heap_tab,
            text="Create Heaps",
            command=self.create_heap
        ).pack(pady=10)

        self.heap_output = tk.Text(heap_tab, height=15)
        self.heap_output.pack(fill="both", expand=True)

        task_tab = ttk.Frame(notebook)
        notebook.add(task_tab, text="Priority Queue")

        ttk.Label(task_tab, text="Priority").pack()

        self.priority_entry = ttk.Entry(task_tab)
        self.priority_entry.pack()

        ttk.Label(task_tab, text="Task").pack()

        self.task_entry = ttk.Entry(task_tab, width=40)
        self.task_entry.pack()

        ttk.Button(
            task_tab,
            text="Add Task",
            command=self.add_task
        ).pack(pady=5)

        ttk.Button(
            task_tab,
            text="Run Tasks",
            command=self.run_tasks
        ).pack(pady=5)

        self.task_output = tk.Text(task_tab, height=20)
        self.task_output.pack(fill="both", expand=True)

    def insert_avl(self):

        try:
            value = int(self.avl_entry.get())
        except:
            return

        self.avl.logs.clear()

        self.avl_root = self.avl.insert(self.avl_root, value)

        self.avl_output.delete(1.0, tk.END)

        self.avl_output.insert(tk.END, f"Inserted {value}\n\n")

        for log in self.avl.logs:
            self.avl_output.insert(tk.END, log + "\n")

        self.avl_output.insert(
            tk.END,
            "\nPreorder Traversal:\n"
        )

        self.avl_output.insert(
            tk.END,
            self.avl.preorder(self.avl_root)
        )

        self.avl_entry.delete(0, tk.END)

    def create_heap(self):

        try:
            data = list(map(int,
                            self.heap_entry.get().split(",")))
        except:
            return

        min_heap = data.copy()
        heapq.heapify(min_heap)

        max_heap = [-x for x in data]
        heapq.heapify(max_heap)

        max_heap = [-x for x in max_heap]

        self.heap_output.delete(1.0, tk.END)

        self.heap_output.insert(
            tk.END,
            f"Original : {data}\n\n"
        )

        self.heap_output.insert(
            tk.END,
            f"Min Heap : {min_heap}\n\n"
        )

        self.heap_output.insert(
            tk.END,
            f"Max Heap : {max_heap}"
        )

    def add_task(self):

        try:
            priority = int(self.priority_entry.get())
        except:
            return

        task = self.task_entry.get()

        heapq.heappush(self.tasks, (priority, task))

        self.task_output.insert(
            tk.END,
            f"Added -> Priority {priority}: {task}\n"
        )

        self.priority_entry.delete(0, tk.END)
        self.task_entry.delete(0, tk.END)

    def run_tasks(self):

        self.task_output.insert(
            tk.END,
            "\nProcessing Tasks\n"
        )

        while self.tasks:
            p, task = heapq.heappop(self.tasks)
            self.task_output.insert(
                tk.END,
                f"Priority {p} -> {task}\n"
            )

root = tk.Tk()
app = Application(root)
root.mainloop()