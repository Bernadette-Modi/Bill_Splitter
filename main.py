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

while True:
    total = float(input("Enter the total amount: ")) 
    if total <= 0:
        continue
    break

while True:
    person = int(input("Enter number of people: "))
    if person <= 0:
        continue
    break 

while True:
    tip = float(input("Enter the tip percentage: "))
    if tip < 0:
        continue
    break

bs = BillSplitter(total, person, tip)
print(f"Each person will have to pay {bs.total_sum():.2f}.")

