import tkinter as tk
from tkinter import messagebox

class StylishCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")
        self.master.config(bg="#f8f9fa")

        self.current_expression = ""

        # Entry field for displaying calculations
        self.display = tk.Entry(master, font=('Helvetica', 32), bd=5, insertwidth=4, width=14, borderwidth=2, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define button layout
        button_labels = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in button_labels:
            self.create_button(text, row, col)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, font=('Helvetica', 24), bg="#ffffff", fg="#333333",
                           command=lambda: self.handle_click(text), relief='raised', bd=3)
        button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

    def handle_click(self, char):
        if char == 'C':
            self.current_expression = ""
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(self.current_expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero.")
                self.current_expression = ""
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                self.current_expression = ""
        else:
            self.current_expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = StylishCalculator(root)
    root.mainloop()
