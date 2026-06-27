#  Expense Tracker

A simple command-line expense tracker built in Python. It lets you add, view, total, and remove expenses, with everything saved to a local text file so your data persists between runs.

##  Features

- **Add Expense** — enter a name and amount, saved to `expenses.txt`
- **View Expenses** — see every expense you've logged so far
- **Calculate Total Spending** — adds up all amounts in `expenses.txt` and shows the total
- **Remove Expense** — delete an expense by name
- Runs in a continuous menu loop until you choose to exit
- Data is stored in a plain text file (`expenses.txt`), so your expenses are saved even after closing the program
- No external dependencies — uses only Python's built-in file handling

##  Tech Stack

- **Language:** Python 3
- **Storage:** Plain text file (`expenses.txt`)
- **Libraries:** None — built entirely with Python's standard file I/O

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/farahnoorcodes/expense-tracker.git
   cd expense-tracker
   ```

2. No additional dependencies needed — just make sure you have Python 3 installed:
   ```bash
   python --version
   ```

##  Usage

Run the script from your terminal:

```bash
python expensetracker.py
```

You'll see a menu with five options:

```
|=========EXPENSE TRACKER=========|
|=================================|

| 1. Add Expense                  |
| 2. View Expenses                |
| 3. Calculate total spending     |
| 4. Remove Expense                |
| 5. Exit                         |
|=================================|
Enter your choice (1-5):
```

**Example — adding and viewing an expense:**
```
Enter your choice (1-5): 1
Enter expense name: Groceries
Enter expense amount: 1500
 Expense added successfully!

Enter your choice (1-5): 2

Your Expenses:
Groceries: 1500
```

**Example — calculating total spending:**
```
Enter your choice (1-5): 3
Total spending: Rs.1500.00
```

A file named `expenses.txt` will be created automatically in the same folder the first time you add an expense.

##  Project Structure

```
expense-tracker/
│
├── expensetracker.py   # Main script
├── expenses.txt         # Auto-generated file storing your expenses (created on first run)
├── README.md             # Project documentation
└── LICENSE                # License file (optional)
```

##  Notes

- Expense names should be unique-ish — removing an expense matches by exact name, so if two expenses share the same name, all matching entries will be removed.
- The amount is currently displayed in Rs. (PKR). Change the print statement in option 3 if you'd like a different currency symbol.
- `expenses.txt` is created automatically — you don't need to create it yourself before running the script.

##  Future Improvements

- Add date/timestamp to each expense entry
- Add expense categories (e.g., food, transport, bills)
- Switch from a text file to a CSV or JSON file for more structured storage
- Add input validation (e.g., reject non-numeric amounts)
- Add a way to edit an existing expense instead of only removing it
- Add monthly/category-wise spending summaries

##  Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repo and submit a pull request.

##  License

This project is open source and available under the [MIT License](LICENSE).

##  Author

**Farah Noor**
- GitHub: [@farahnoorcodes](https://github.com/farahnoorcodes)

