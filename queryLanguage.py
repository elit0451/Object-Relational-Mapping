import re

def myQuery(command):
	select = '*'
	fromTable = ''
	where = ''
	joins = ''
	
	# Check if we don't have WHERE clause
	if(command.count('(') <= 0):
		# Regex for matching the string 'table' and/or 'table.field'
		regexExp = '(\w*)\.?(\w*)?'
		regexPattern = re.compile(regexExp)
		match = regexPattern.search(command)
		
		# Check if we have a field after the .
		if(len(match.groups()[1]) > 0):
			select = match.groups()[1]
		fromTable = match.groups()[0]
		
	elif(command.count('.') <= 0):
		# Regex for matching the commands in the parenthesis
		regexExp = '\((.*?)\|(.*?)\)'
		regexPattern = re.compile(regexExp)
		match = regexPattern.search(command)
		
		# Check if we have a condition after the |
		if(len(match.groups()[1]) > 0):
			where = match.groups()[1]
		fromTable = match.groups()[0]
	else:		
		# Regex for matching the commands in the parenthesis
		regexExp = '\((.*?)\|(.*?)\)'
		regexPattern = re.compile(regexExp)
		match = regexPattern.search(command)
		
		# Check if we have a condition after the |
		if(len(match.groups()[1]) > 0):
			where = match.groups()[1]
		fromTable = match.groups()[0]
		
		# Regex for matching all the tables fields
		regexExp = '\.(\w*)?'
		regexPattern = re.compile(regexExp)
		
		joinTable = fromTable
		
		for table in re.findall(regexPattern, command):
			if(table.islower()):
			# Select specific field if we have one specified 
				select = select[:-1] + table
			else:
			# Select all the fields 
				select = table + '.*'
				
				if(table == 'Customer' or joinTable == 'Customer'):
					field = 'customer_id'
				elif(table == 'Product' or joinTable == 'Product'):
					field = 'product_id'
				else:
					field = joinTable.lower() + '_id'
					
				joins += '\nINNER JOIN ' + table + ' ON ' + table + '.' + field + ' = ' + joinTable + '.' + field
				joinTable = table
	
	fullSQL = 'SELECT ' + select + '\n'
	fullSQL += 'FROM ' + fromTable + '\n'
	
	if(len(where)>0):
		fullSQL += 'WHERE ' + where
	if(len(joins) > 0):
		fullSQL += joins
	
	print(fullSQL)

# Visualize queries	
myQuery("Customer")
print("\n-----------------------------------")
myQuery("Customer.name")
print("\n-----------------------------------")
myQuery("(Customer|name='Joe')")
print("\n-----------------------------------")
myQuery("(Customer|name='Joe').Orders")
print("\n-----------------------------------")
myQuery("(Customer|name='Joe').Orders.OrderLine.Product")
print("\n-----------------------------------")
myQuery("(Orders|total > 200).Customer.name")