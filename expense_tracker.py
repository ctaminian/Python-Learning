def main():
    summary_of_expenses = {}
    while True:
        try:
            expense = input("Enter an expense (Category, Amount) or 'done' to finish: ").strip()
            
            if expense.lower() == "done":
                break
            
            expense_details = expense.split(",")
            if len(expense_details) != 2:
                raise ValueError
            
            category = expense_details[0].strip()
            amount = float(expense_details[1].strip())
            
            if not category or amount <= 0:
                raise ValueError

            summary_of_expenses[category] = summary_of_expenses.get(category, 0) + amount

        except ValueError:
            print("Invalid Input. Please enter in the format 'Category, Positive Amount'. Example: Food, 12.50")

    print("\nSummary of expenses:")
    total_expenses = sum(summary_of_expenses.values())

    for category, amount in summary_of_expenses.items():
        print(f"{category}: ${amount:.2f}")

    print(f"Total: ${total_expenses:.2f}")

if __name__ == "__main__":
    main()