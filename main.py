print("\n Welcome to the bill splitter!")
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

def get_valid_input(prompt, type_func, condition):
    while True:
        try:
            value = type_func(input(prompt))
            if condition(value):
                return value
            else:
                print("Invalid input. Please enter a valid value.")
        except ValueError:
            print("Invalid input. Please enter a number.")

total = get_valid_input("Enter the total amount: $", float, lambda x: x > 0)
person = get_valid_input("Enter the number of people: ", int, lambda x: x > 0)
tip = get_valid_input("Enter the tip percentage: ", float, lambda x: x >= 0)

bs = BillSplitter(total, person, tip)
print(f"Each person will have to pay {bs.total_sum():.2f}.")

