import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())  
        num2 = float(entry2.get())
        product = num1 * num2
        result_lbl.config(text=f"Product: {product}")
    except ValueError:
        result_lbl.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("Multiplication Calculator")
root.geometry("300x300")

tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.pack(pady=10)

result_lbl = tk.Label(root, text="Product: ")
result_lbl.pack(pady=5)

root.mainloop()