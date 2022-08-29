class Rent():
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.total_cash_flow = None
        self.investment = {}


    def income_calc(self):
        while True:
            other_income = input("Do you have a source of income? y/n ").lower()
            if other_income == "y":
                source_income = input("what is the name of that source? ").lower()
                if source_income not in self.income:
                    income_amount = int(input("How much income are you making from that source? "))
                    self.income[source_income] = income_amount
                else:
                    return "That source has already been added"
            else:
                break
            print(self.income)
        total_income = sum(self.income.values())
        return f"Your monthly income equals: {total_income}"

    def expenses_calc(self):
        while True:
            other_expenses = input("Do you have any expenses? y/n ").lower()
            if other_expenses == "y":
                source_expenses = input("what is the name of that expense? ").lower()
                if source_expenses not in self.expenses:    
                    expenses_amount = int(input("What is the total of that expense? "))
                    self.expenses[source_expenses] = expenses_amount
                else:
                    return "That expense already exists"
            else:
                break
            print(self.expenses)
        total_expenses = sum(self.expenses.values())
        return f"Your monthly expenses equals: {total_expenses}"

class Cash(Rent):

    def cash_flow(self):
        total_income = sum(self.income.values())
        total_expenses = sum(self.expenses.values())

        self.total_cash_flow = total_income - total_expenses

        return f"Your monthly cash flow is: {self.total_cash_flow}"

    def roi(self):
        
        while True:
            investment_ = input("Did you make an investment on the rental property? y/n ").lower()
            if investment_ == "y":
                investment_type = input("What is the type of investment you made? ").lower()
                investment_amount = int(input("How much did you pay for that investment? "))
                self.investment[investment_type] = investment_amount
            else:
                break
        investment_total = sum(self.investment.values())

        print(self.investment)
        print(investment_total)
        
        roi_total = ((self.total_cash_flow * 12) / investment_total) * 100
        return round(roi_total,2)
    
    def roi_rate(self):
        roi_return = Cash.roi(self)
        print(f"Your ROI is: {roi_return}%")

        if roi_return < 8:
            return "That is a bad ROI on the property, maybe hire a better agent next time."
        elif roi_return > 8 and roi_return <= 12:
            return "That is a good ROI rate, but could be better."
        elif roi_return > 12:
            return "That is an amzing return on the property! You are a pro at this."

saad_cash = Cash()

def run():
        
    while True:
        choice = input("""
            Welcome to your personal calculator for rental property!
            Let's get started. Here are your options:
            [1] Income_total
            [2] Expenses_total
            [3] Cash Flow
            [4] Cash on cash ROI and ROI rate
            [5] Quit
            """)
        if choice == "1":
            print(saad_cash.income_calc())
        if choice == "2":
            print(saad_cash.expenses_calc())
        elif choice == "3":
            print(saad_cash.cash_flow())
        elif choice == "4":
            print(saad_cash.roi_rate())
        elif choice == "5":
            print("Thank you for using the services. Please come back if you have any other calculations! ")
            break


run()


