import tkinter as tk
from tkinter import messagebox
print("S104 Pratik")
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
            return "Inserted " + str(data) + " into empty list."
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return "Inserted " + str(data) + " at the beginning."

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return "Inserted " + str(data) + " into empty list."
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp
        return "Inserted " + str(data) + " at the end."

    def insert_at_position(self, data, position):
        if position < 1:
            return "Error: Position must be 1 or greater."

        if position == 1:
            return self.insert_at_beginning(data)

        new_node = Node(data)
        temp = self.head
        count = 1
        
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            return "Error: Position out of bounds."

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node
            
        temp.next = new_node
        return "Inserted " + str(data) + " at position " + str(position) + "."

    def delete_by_value(self, key):
        if self.head is None:
            return "Error: List is empty. Nothing to delete."

        temp = self.head

        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return "Deleted node with value " + str(key) + "."

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            return "Error: Node with value " + str(key) + " not found."

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

        return "Deleted node with value " + str(key) + "."


class DLLGuiApp:
    def __init__(self, root):
        self.dll = DoublyLinkedList()
        self.root = root
        self.root.title("Linked List Operations Menu")
        self.root.geometry("550x450")
        self.root.configure(bg="#f0f0f0")

        # Menu Header (Matching Back.BLUE and Fore.WHITE)
        self.header = tk.Label(
            root, 
            text=" Linked List Operations Menu ", 
            bg="blue", 
            fg="white", 
            font=("Arial", 16, "bold"),
            pady=10
        )
        self.header.pack(fill=tk.X)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#f0f0f0", pady=15)
        self.input_frame.pack()

        tk.Label(self.input_frame, text="Value:", bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)
        self.val_entry = tk.Entry(self.input_frame, font=("Arial", 11), width=10)
        self.val_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Position:", bg="#f0f0f0", font=("Arial", 11)).grid(row=0, column=2, padx=5, pady=5)
        self.pos_entry = tk.Entry(self.input_frame, font=("Arial", 11), width=5)
        self.pos_entry.grid(row=0, column=3, padx=5, pady=5)

        # Button Frame
        self.btn_frame = tk.Frame(root, bg="#f0f0f0")
        self.btn_frame.pack(pady=10)

        # Action Buttons (Matching Fore.CYAN and Fore.WHITE styling concepts)
        tk.Button(self.btn_frame, text="1. Insert at Beginning", width=20, font=("Arial", 10), command=self.ins_beginning).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.btn_frame, text="2. Insert at End", width=20, font=("Arial", 10), command=self.ins_end).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.btn_frame, text="3. Insert at Position", width=20, font=("Arial", 10), command=self.ins_position).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.btn_frame, text="4. Delete by Value", width=20, font=("Arial", 10), command=self.del_value).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.btn_frame, text="5. Traverse List", width=20, font=("Arial", 10), command=self.traverse).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self.btn_frame, text="6. Exit", width=20, font=("Arial", 10), bg="#ff4d4d", fg="white", command=root.quit).grid(row=2, column=1, padx=10, pady=5)

        # Status Label (For operation outcomes)
        self.status_label = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="#f0f0f0", pady=10)
        self.status_label.pack()

        # Visual List Display Frame (Matching Black text on White block display)
        tk.Label(root, text="List Traversal:", font=("Arial", 12, "underline"), bg="#f0f0f0").pack(anchor="w", padx=20)
        
        self.display_frame = tk.Frame(root, bg="#e0e0e0", bd=2, relief="groove", height=60)
        self.display_frame.pack(fill=tk.X, padx=20, pady=10)
        self.display_frame.pack_propagate(False)

        self.traverse()

    def update_status(self, message):
        if "Error" in message:
            self.status_label.config(text=message, fg="red")
        elif "Deleted" in message:
            self.status_label.config(text=message, fg="orange")
        else:
            self.status_label.config(text=message, fg="green")

    def render_visual_list(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.display_frame, bg="#e0e0e0", height=50, bd=0, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        temp = self.dll.head
        x_pos = 20
        y_pos = 15

        if temp is None:
            canvas.create_text(x_pos, y_pos + 10, text="List is empty: None", anchor="w", fill="cyan", font=("Arial", 11, "bold"))
            return

        while temp:
            # Draw White Node Block with Black Text
            text_id = canvas.create_text(x_pos + 10, y_pos + 10, text=f" {temp.data} ", anchor="w", fill="black", font=("Arial", 11, "bold"))
            bbox = canvas.bbox(text_id)
            rect_id = canvas.create_rectangle(bbox[0]-5, bbox[1]-2, bbox[2]+5, bbox[3]+2, fill="white", outline="black")
            canvas.tag_raise(text_id, rect_id)
            
            x_pos = bbox[2] + 5
            temp = temp.next
            
            # Draw the "<->" link pointer
            if temp:
                pointer_id = canvas.create_text(x_pos + 5, y_pos + 10, text=" <-> ", anchor="w", fill="purple", font=("Arial", 11, "bold"))
                p_bbox = canvas.bbox(pointer_id)
                x_pos = p_bbox[2] + 5
        
        canvas.create_text(x_pos + 5, y_pos + 10, text=" -> None", anchor="w", fill="black", font=("Arial", 11))

    def ins_beginning(self):
        val = self.val_entry.get().strip()
        if not val:
            self.update_status("Error: Value field cannot be empty.")
            return
        msg = self.dll.insert_at_beginning(val)
        self.update_status(msg)
        self.render_visual_list()
        self.val_entry.delete(0, tk.END)

    def ins_end(self):
        val = self.val_entry.get().strip()
        if not val:
            self.update_status("Error: Value field cannot be empty.")
            return
        msg = self.dll.insert_at_end(val)
        self.update_status(msg)
        self.render_visual_list()
        self.val_entry.delete(0, tk.END)

    def ins_position(self):
        val = self.val_entry.get().strip()
        pos_str = self.pos_entry.get().strip()
        if not val or not pos_str:
            self.update_status("Error: Value and Position fields required.")
            return
        try:
            pos = int(pos_str)
        except ValueError:
            self.update_status("Error: Position must be a valid integer.")
            return
            
        msg = self.dll.insert_at_position(val, pos)
        self.update_status(msg)
        self.render_visual_list()
        self.val_entry.delete(0, tk.END)
        self.pos_entry.delete(0, tk.END)

    def del_value(self):
        val = self.val_entry.get().strip()
        if not val:
            self.update_status("Error: Enter value to delete.")
            return
        msg = self.dll.delete_by_value(val)
        self.update_status(msg)
        self.render_visual_list()
        self.val_entry.delete(0, tk.END)

    def traverse(self):
        self.render_visual_list()
        if self.dll.head is None:
            self.update_status("List is empty.")
        else:
            self.update_status("List traversed successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DLLGuiApp(root)
    root.mainloop()
