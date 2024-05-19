# Budget-App
The Budget App helps manage different budget categories such as food, clothing, and entertainment. This application is built using the Category class in budget.py, which allows users to track their expenses and deposits efficiently.
Features

The Category class provides the following functionalities:

#  1- Initialization:
        
        * When a category object is created, it is initialized with the name of the category.
        
        * An instance variable called a ledger is a list that records all the transactions.

#  2- Deposit Method:
        
        * Accepts an amount and an optional description (defaults to an empty string if not provided).
        
        * Appends an object to the ledger list in the form of {"amount": amount, "description": description}.

#  3- Withdraw Method:
        
        * Similar to the deposit method, but the amount is stored as a negative number.
        
        * If there are insufficient funds, nothing is added to the ledger.
        
        * Returns True if the withdrawal is successful, and False otherwise.

#  4- Get Balance Method:
       
        * Returns the current balance of the budget category based on the deposits and withdrawals.

#  5- Transfer Method:
       
       * Accepts an amount and another budget category as arguments.
       
       * Adds a withdrawal to the current category with the description "Transfer to [Destination Budget Category]".
       
       * Adds a deposit to the destination category with the description "Transfer from [Source Budget Category]".
       
       * If there are insufficient funds, nothing is added to either ledger.
       
       * Returns True if the transfer is successful, and False otherwise.

#  6- Check Funds Method:
       
       * Accepts an amount as an argument.
       
       * Returns False if the amount is greater than the current balance, True otherwise.
       
       * Used by both the withdrawal and transfer methods.

#  7- String Representation:
       
       * When the budget object is printed, it displays:
            
            * A title line of 30 characters where the name of the category is centered within a line of * characters.
            * A list of the items in the ledger. Each line shows the description and amount.
                * The first 23 characters of the description are displayed.
                * The amount is right-aligned, with two decimal places, and displays a maximum of 7 characters.
            * A-line displaying the total balance of the category.

# Example:

    from budget import Category

    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    print(food)
    print(clothing)

# Output:

    *************Food*************
    initial deposit        1000.00
    groceries               -10.15
    restaurant and more food for dessert -15.89
    Transfer to Clothing    -50.00
    Total: 923.96
    ***********Clothing***********
    Transfer from Food       50.00
                            -25.55
    Total: 24.45


