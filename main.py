import tkinter as tk
from tkinter import messagebox

class BillSplitter:

    def __init__(self, total_bill: float, num_people: int, tip_percentage: float):
        self.total_bill = total_bill
        self.num_people = num_people
        self.tip_percentage = tip_percentage

    def per_person(self) -> float:
        return self.total_bill / self.num_people

    def tip_calculation(self) -> float:
        return self.tip_percentage / 100 * self.total_bill

    def total_sum(self) -> float:
        if self.tip_percentage > 0:
            return self.per_person() + self.tip_calculation()
        return self.per_person()

# def get_valid_input(prompt, type_func, condition):
#     while True:
#         try:
#             value = type_func(input(prompt))
#             if condition(value):
#                 return value
#             else:
#                 print("Invalid input. Please enter a valid value.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# total = get_valid_input("Enter the total amount: $", float, lambda x: x > 0)
# person = get_valid_input("Enter the number of people: ", int, lambda x: x > 0)
# tip = get_valid_input("Enter the tip percentage: ", float, lambda x: x >= 0)

# bs = BillSplitter(total, person, tip)
# print(f"Each person will have to pay {bs.total_sum():.2f}.")

def calculate():
    try:
        total = float(entry_total.get())
        person = int(entry_people.get())
        tip = float(entry_tip.get())

        if total <= 0 or person <= 0 or tip < 0:
            messagebox.showerror("Input Error", "Please enter a valid positive values!")
            return
        
        bs = BillSplitter(total, person, tip)
        result_label.config(text=f"Each person pays: ${bs.total_sum():.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Bill Splitter")
root.geometry("300x300")
root.configure(bg="light blue")

tk.Label(root, text="Total Bill: ", bg=("light blue")).pack()
entry_total = tk.Entry(root)
entry_total.pack()

tk.Label(root, text="Number of People:", bg=("light blue")).pack()
entry_people = tk.Entry(root)
entry_people.pack()

tk.Label(root, text="Tip Percentage: ", bg=("light blue"), fg=("Black")).pack()
entry_tip = tk.Entry(root)
entry_tip.pack()

entry_total.bind("<Return>", lambda event: calculate())
entry_people.bind("<Return>", lambda event: calculate())
entry_tip.bind("<Return>", lambda event: calculate())

btn_calculate = tk.Button(root, text="Split", command=calculate, fg=("black"))
btn_calculate.pack()

result_label = tk.Label(root, bg=("light blue"), text="")
result_label.pack()

root.mainloop()
