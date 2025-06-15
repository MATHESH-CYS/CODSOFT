import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("User Input Calculator")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#222831")

        self.result_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Enter First Number:", bg="#222831", fg="white", font=("Arial", 12)).pack(pady=5)
        self.num1_entry = tk.Entry(self.root, font=("Arial", 12))
        self.num1_entry.pack(pady=5)

        tk.Label(self.root, text="Enter Operation (+, -, *, /):", bg="#222831", fg="white", font=("Arial", 12)).pack(pady=5)
        self.op_entry = tk.Entry(self.root, font=("Arial", 12))
        self.op_entry.pack(pady=5)

        tk.Label(self.root, text="Enter Second Number:", bg="#222831", fg="white", font=("Arial", 12)).pack(pady=5)
        self.num2_entry = tk.Entry(self.root, font=("Arial", 12))
        self.num2_entry.pack(pady=5)

        calc_btn = tk.Button(self.root, text="Calculate", font=("Arial", 12), bg="#00ADB5", fg="white", command=self.calculate)
        calc_btn.pack(pady=10)

        self.result_label = tk.Label(self.root, textvariable=self.result_text, font=("Arial", 14), bg="#222831", fg="#FFD369")
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            op = self.op_entry.get()

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            else:
                self.result_text.set("Invalid Operation")
                return

            self.result_text.set(f"Result: {result}")
        except ValueError:
            self.result_text.set("Enter valid numbers")
        except ZeroDivisionError:
            self.result_text.set("Division by zero error")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()
