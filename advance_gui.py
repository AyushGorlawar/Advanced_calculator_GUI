import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced GUI")

        self.entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right', borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Define buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create and place buttons in the grid
        for button_text, row_val, col_val in buttons:
            tk.Button(root, text=button_text, width=5, height=2,
                      command=lambda b=button_text: self.on_click(b) if b != '=' else self.calculate_result()).grid(
                row=row_val, column=col_val)

        # Clear button
        tk.Button(root, text='C', width=5, height=2, command=self.clear_entry).grid(row=5, column=0)

        tk.Button(root, text='Exit', width=5, height=2, command=self.exit_app).grid(row=5, column=1)

    def on_click(self, button_value):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + str(button_value))

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate_result(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            messagebox.showerror("Error", "Invalid Input")

    def exit_app(self):
        self.root.destroy()

# Create the main window
root = tk.Tk()
app = CalculatorApp(root)

root.mainloop()
