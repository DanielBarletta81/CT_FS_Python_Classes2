##

#: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc.,
#  ensuring that budget details remain private and are accessed or modified through public methods.

#Task 1: Define Budget Category Class Create a class `BudgetCategory` 
# with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.


class BudgetCategory:
  
    def __init__(self, category, budget_amt):
        #make private attributes for category and budget amount
        self.__budget_amt = budget_amt
        self.__category = category
    # getters and setters
    def get_category(self):
        return self.__category

    def set_category(self, new_category):
        self.__category = new_category

    def get_budget_amt(self):
        return self.__budget_amt

    def set_budget_amt(self, new_budget_amt):
        self.__budget_amt = new_budget_amt

#Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust
#  the budget accordingly.
#  Validate the expense amount before making deductions from the budget.

#Expected Outcome: Ability to track expenses per category and update the remaining budget safely.


# method to display category details

    def show_category_summary(self):
       
       print(f'Budget Category: {self.get_category()}\n Balance: {self.get_budget_amt()}')
       
  # method to calculate expenses
  #   
    def incur_expense(self,amount):
       if amount > 0:
           self.set_budget_amt(self.get_budget_amt() - amount)
           print(f'Budget {self.__category} decreased by {amount}.')
       else:
           print("Error.")
       
       

# method to add money to budget
    def add_to_budget(self,amount):
       if amount > 0:
           self.set_budget_amt(self.get_budget_amt() + amount)
           print(f'Budget {self.__category} increased by {amount}.')
       else:
           print("Error.")
            
   # create instances of Class BudgetCategory

budget = BudgetCategory("Entertainment", 1000)
print(f'Category: {budget.get_category()}')
print(f'Budgeted Amount: {budget.get_budget_amt()}')



food_budget = BudgetCategory("Food", 1200)
print(f'Category: {food_budget.get_category()}')
print(f'Budgeted Amount: {food_budget.get_budget_amt()}')

travel_budget = BudgetCategory("Travel", 3500)

travel_budget.incur_expense(2500)

travel_budget.show_category_summary()


food_budget.show_category_summary()