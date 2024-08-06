# Example budget data
budgets = {
    'groceries': 300,  # Monthly budget limit for groceries
    'utilities': 100,  # Monthly budget limit for utilities
    'entertainment': 150,
    'dining out': 200,
    'transport': 100
}

# Example spending data
spending = {
    'groceries': 0,
    'utilities': 0,
    'entertainment': 0,
    'dining out': 0,
    'transport': 0
}

def update_spending(category, amount):
    if category in spending:
        spending[category] += amount
    else:
        print(f"Category '{category}' not found.")

def check_budget(category):
    if category not in spending:
        return "Category not found."

    spent = spending[category]
    budget = budgets.get(category, 0)

    if spent <= budget:
        return f"Within budget: ${budget - spent} remaining."
    else:
        return f"Exceeded budget by ${spent - budget}."

def display_budget_status():
    for category in spending:
        status = check_budget(category)
        print(f"Category: {category}\nSpent: ${spending[category]}\nStatus: {status}\n")

# Example usage
update_spending('groceries', 50)
update_spending('utilities', 110)
display_budget_status()
