""" 
Retirement Fund Calculator

class Retirement:
that initializes 2 variables in  def __init__(self, amount): a float variable self.balance that starts as equal to the amount and an integer self.year that starts as 1.
Provide 2 additional functions within the class:
•	def deposit(self, amount) to add to the balance variable the given amount.
•	def yearly_interest(self, percent) to multiply the balance by 1 + (percent/100). This function also adds 1 year onto the year 
•	Both functions should return (not print!) a string "In Year x, your current balance is $___" 

In your main module:
•	Create a retirement object,  my_fund, that starts the fund at 2000.
•	Then, execute the following code:

"""
  
class Retirement:
    def __init__(self,amount):
        self.balance = amount
        self.year = 1
        
    def deposit(self,amount):
        self.balance += amount
        return "In Year %d, your current balance is $%.0f" % (self.year,self.balance)
    
    def yearly_interest(self,percent):
        self.balance *= 1+percent/100
        self.year += 1
        return "In Year %d, your current balance is $%.0f" % (self.year,self.balance)