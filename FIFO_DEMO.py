import tkinter as tk
from tkinter import messagebox

class FifoDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Demostración de FIFO (Cola)")

        self.fifo_queue = []

        # Configuración de la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Cola (FIFO)
        tk.Label(self, text="Cola (FIFO)").pack(pady=10)
        self.fifo_listbox = tk.Listbox(self)
        self.fifo_listbox.pack(pady=5)

        self.fifo_entry_var = tk.StringVar()  # Correctly initialize the StringVar
        tk.Entry(self, width=20, textvariable=self.fifo_entry_var).pack(pady=5)
        tk.Button(self, text="Añadir a Cola", command=self.add_to_fifo).pack(pady=5)
        tk.Button(self, text="Eliminar de Cola", command=self.remove_from_fifo).pack(pady=5)

    def add_to_fifo(self):
        item = self.fifo_entry_var.get()
        if item:
            self.fifo_queue.append(item)
            self.update_fifo_display()
            self.fifo_entry_var.set("")

    def remove_from_fifo(self):
        if self.fifo_queue:
            self.fifo_queue.pop(0)
            self.update_fifo_display()
        else:
            messagebox.showwarning("Advertencia", "La cola está vacía")

    def update_fifo_display(self):
        self.fifo_listbox.delete(0, tk.END)
        for item in self.fifo_queue:
            self.fifo_listbox.insert(tk.END, item)

if __name__ == "__main__":
    app = FifoDemo()
    app.mainloop()
