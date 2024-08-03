import tkinter as tk
from tkinter import messagebox

class LifoDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Demostración de LIFO (Pila)")

        self.lifo_stack = []

        # Configuración de la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Pila (LIFO)
        tk.Label(self, text="Pila (LIFO)").pack(pady=10)
        self.lifo_listbox = tk.Listbox(self)
        self.lifo_listbox.pack(pady=5)

        self.lifo_entry_var = tk.StringVar()  # Correctly initialize the StringVar
        tk.Entry(self, width=20, textvariable=self.lifo_entry_var).pack(pady=5)
        tk.Button(self, text="Añadir a Pila", command=self.add_to_lifo).pack(pady=5)
        tk.Button(self, text="Eliminar de Pila", command=self.remove_from_lifo).pack(pady=5)

    def add_to_lifo(self):
        item = self.lifo_entry_var.get()
        if item:
            self.lifo_stack.append(item)
            self.update_lifo_display()
            self.lifo_entry_var.set("")

    def remove_from_lifo(self):
        if self.lifo_stack:
            self.lifo_stack.pop()
            self.update_lifo_display()
        else:
            messagebox.showwarning("Advertencia", "La pila está vacía")

    def update_lifo_display(self):
        self.lifo_listbox.delete(0, tk.END)
        for item in reversed(self.lifo_stack):
            self.lifo_listbox.insert(tk.END, item)

if __name__ == "__main__":
    app = LifoDemo()
    app.mainloop()
