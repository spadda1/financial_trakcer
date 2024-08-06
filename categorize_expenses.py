# Define categories and associated keywords
categories = {
    'groceries': ['milk', 'bread', 'eggs', 'cheese', 'vegetables', 'fruit'],
    'utilities': ['electricity', 'water', 'gas'],
    'entertainment': ['movie', 'concert', 'event'],
    'dining out': ['restaurant', 'cafe', 'bar'],
    'transport': ['bus', 'train', 'taxi', 'fuel']
}

def categorize_expense(text):
    """
    Categorize an expense based on the provided text.

    :param text: String containing the description of the expense.
    :return: Category of the expense as a string.
    """
    expense_category = 'others'  # Default category if no keywords match
    # Convert text to lowercase for case-insensitive comparison
    text = text.lower()
    
    # Check each category and its keywords
    for category, keywords in categories.items():
        if any(keyword in text for keyword in keywords):
            expense_category = category
            break
            
    return expense_category

# Example usage
if __name__ == "__main__":
    # Example text inputs
    example_texts = [
        "Bought milk and bread from the grocery store.",
        "Paid the electricity bill for the month.",
        "Went to the cinema for a movie night.",
        "Dinner at a local restaurant.",
        "Filled up the car with fuel."
    ]
    
    # Categorize and print each example text
    for text in example_texts:
        category = categorize_expense(text)
        print(f"Text: {text}\nCategory: {category}\n")
