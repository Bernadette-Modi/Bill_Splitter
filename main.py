print("\n Welcome to the bill splitter!")
class BillSplitter:

    def __init__(self, total_bill, num_people, tip_calculation):
        self.total_bill = total_bill
        self.num_people = num_people
        self.tip_calcualtion = tip_calculation

    def per_person(self) -> float:
        self.total_bill / self.num_people

    def tip_calculation(self) -> float:
        self.tip_calcualtion / 100 * self.total_bill

    def total_sum(self) -> float:
        self.per_person() + self.tip_calcualtion()

    