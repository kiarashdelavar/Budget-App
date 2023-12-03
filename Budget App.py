class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.category.center(30, "*")
        items = "\n".join(
            f"{item['description'][:23]:<23}{item['amount']:.2f}" for item in self.ledger
        )
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}\n{total}"

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent_percentages = [
        (category.get_balance() / sum(c.get_balance() for c in categories)) * 100
        for category in categories
    ]
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        chart += " ".join("o" if percent >= i else " " for percent in spent_percentages)
        chart += "  \n"
    chart += "    ----------\n     "
    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += " \n     "
    return chart

# Example usage:
food_category = Category("Food")
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
clothing_category = Category("Clothing")
food_category.transfer(50, clothing_category)

print(food_category)
print(clothing_category)
chart = create_spend_chart([food_category, clothing_category])
print(chart)
