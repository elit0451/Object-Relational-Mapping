import json

source = '''{"schemaName": "MicroShop",
  "entities": [
  	{"Customer": {
  		"name": "String",
  		"orders" :"*Order"}},
  	{"Order" :{
  		"date": "String",
  		"total": "Number",
  		"customer": "Customer",
  		"lines": "*OrderLine" }},
  	{"OrderLine" : {
  		"order": "Order",
  		"product": "Product",
  		"count": "Number",
  		"total": "Number" }},
  	{"Product" : {
  		"name": "String",
  		"price" :"Number"}}
  ]
}'''

# SQL script composition	
def generateSQLHeader(schemaName):
	headerSQL = 'DROP DATABASE IF EXISTS `' + schemaName + '`;\n\n'
	headerSQL += 'CREATE DATABASE `' + schemaName + '`;\n\n'
	headerSQL += 'USE `' + schemaName + '`;'
	
	return headerSQL

	
def generateSQLEntities(entities):
	finalSQL = ''
	for obj in entities:
		for entityName in obj:
			finalSQL += 'DROP TABLE IF EXISTS `' + entityName + '`;\n'
			finalSQL += 'CREATE TABLE `' + entityName + '`(\n'
			finalSQL += '\t' + entityName.lower() + '_id INT,\n'
			for field in obj[entityName]:
				fieldName = field
				fieldType = obj[entityName][field]
				if(fieldType == 'String'):
					fieldType = 'VARCHAR(100)'
				elif(fieldType == 'Number'):
					fieldType = 'INT'
				elif(fieldType.startswith('*')):
					fieldType = ''
				else:
					fieldName += '_id'
					fieldType = 'INT'
				if(len(fieldType) > 0 ):
					finalSQL += '\t' + fieldName + ' ' + fieldType + ',\n'
			finalSQL += '\tprimary key(' + entityName.lower() + '_id)\n'
			finalSQL += ');\n\n'
				
	return finalSQL
	
def composeSQLScript(jsonObj):
	script = generateSQLHeader(jsonObj['schemaName']) 
	script += '\n\n' + generateSQLEntities(jsonObj['entities'])
	
	scriptFile = open(jsonObj['schemaName'] + '.sql', 'w')
	scriptFile.write(script)
	scriptFile.close()
	
	print('File ' + jsonObj['schemaName'] + '.sql has been created!')
	
# C# files composition	
def generateCSClass(entity):
	finalCS = ''
	for entityName in entity:
		finalCS += 'public class ' + entityName + '\n{\n'
		constructor = '\n\tpublic ' + entityName + '(){}\n'
		constructor += '\n\tpublic ' + entityName + '('
		constructorBody = ''
		for field in entity[entityName]:
			fieldName = field
			fieldType = entity[entityName][field]
			if(fieldType == 'String'):
				fieldType = 'string'
			elif(fieldType == 'Number'):
				fieldType = 'int'
			elif(fieldType.startswith('*')):
				fieldType = 'List<' + fieldType[1:] + '>'
			else:
				fieldType = fieldName.capitalize()
			if(len(fieldType) > 0 ):
				finalCS += '\tpublic ' + fieldType + ' ' + fieldName.capitalize() + ' { get; set; }\n'
				constructor += fieldType + ' ' + fieldName + ', '
				constructorBody += '\t\t' + fieldName.capitalize() + ' = ' + fieldName + ';\n'
		#removing the whitespace and the comma (added 2 lines above)
		constructor = constructor[:-2]
		constructor += ')\n\t{\n'
		finalCS += constructor + constructorBody
		finalCS += '\t}\n}\n'
				
	return finalCS
	
def composeCSClass(jsonObj):
	for entity in jsonObj['entities']:
		classBody = generateCSClass(entity)
		
		for entityName in entity:
			scriptFile = open(entityName + '.cs', 'w')
			scriptFile.write(classBody)
			scriptFile.close()
			
			print('File ' + entityName + '.cs has been created!')
		
		
jsonObj = json.loads(source)

# Creating the files
composeSQLScript(jsonObj)
composeCSClass(jsonObj)
