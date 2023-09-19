def truncate(n):
	multiplier = 10
	return int(n * multiplier) / multiplier

def getTotals(categories):
	total = 0
	breakdown = []
	for category in categories:
		total += category.get_withdrawls()
		breakdown.append(category.get_withdrawls())
	rounded = list(map(lambda x: truncate(x/total), breakdown))
	return rounded

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    totals = getTotals(categories)
    
    # Calculate the max of weight
    max_name_length = max(len(category.name) for category in categories)
    
    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for total in totals:
            if total * 100 >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    for i in range(max_name_length):
        res += "     "
        for category in categories:
            if i < len(category.name):
                res += category.name[i] + "  "
            else:
                res += "   "
        if i < max_name_length - 1:
            res += "\n"

    return res


class Category:
	def __init__(self, name):
		self.name = name
		self.ledger = list()

	def __str__(self):
		title = f"{self.name:*^30}\n"
		items = ""
		total = 0
		for item in self.ledger:
			items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

			total += item['amount']
		output = title + items + "Total: " + str(total)
		return output

	def deposit(self, amount, description = ""):
		"""
		A deposit method that accepts an amount and description.
		If no description is given, it should default to an empty string. 
		The method should append an object to the ledger list in the form
		of {"amount": amount, "description": description}.
		"""

		self.ledger.append({"amount": amount, "description": description})


	def withdraw(self, amount, description = ""):
		"""
		A withdraw method that is similar to the deposit method, but the
		amount passed in should be stored in the ledger as a negative number.
		If there are not enough funds, nothing should be added to the ledger.
		This method should return True if the withdrawal took place, and 
		False otherwise.
		"""
		if self.check_funds(amount):
			self.ledger.append({"amount": -amount, "description": description})
			return True
		return False

	def get_balance(self):
	    total_cash = 0
	    for item in self.ledger:
	        total_cash += item["amount"]
	    return total_cash


	def transfer(self, amount, category):
		if(self.check_funds(amount)):
			self.withdraw(amount, "Transfer to " + category.name)
			category.deposit(amount, "Transfer from " + self.name)
			return True
		return False

	def check_funds(self, amount):
    		return self.get_balance() >= amount


	def get_withdrawls(self):
		total = 0
		for item in self.ledger:
			if item["amount"] < 0:
				total += item["amount"]
		return total

