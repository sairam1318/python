# CRUD framweork using sqlite3
import sqlite3
dataBaseName = "data.db"
tableName = "BANK_CUSTOMER_DETAILS"
menuFileName = "menu.cfg"

connection = sqlite3.connect(dataBaseName) 
fields = []
dataType = []

def getFields():

	metadata = connection.execute("PRAGMA TABLE_INFO({})".format(tableName))
	for field in metadata:
		dataType.append(field[2])
		fields.append(field[1])

def addRecord():

	values = ""
	counter = 0
	fieldList = []

	for field in fields:
		if dataType[counter] == 'INT':
			storeData = int(input("\nEnter the " + field + ": "))
			fieldList.append(storeData)
		else:
			storeData = input("\nEnter the {}: ".format(field))
			fieldList.append(storeData)
		counter += 1

	print(counter)
	connection.execute("INSERT INTO {} VALUES {}".format(tableName, tuple(fieldList)))
	connection.commit()

def readRecords():

	cursor = connection.execute("SELECT * FROM {}".format(tableName))

	for field in fields:
		print(field, end = " ")

	for data in cursor:
		print("\n")
		for item in data:
			print(item, end = " ")
		

def updateRecord():

	cursor = connection.execute("SELECT * FROM {}".format(tableName))
	dataToBeUpdated = int(input("Enter data to be updated: "))
	found = 0
	for data in cursor:
		if data[0] == dataToBeUpdated:
			print("Choose data to be updated: ")
			counter = 1
			for field in fields:
				if field == fields[0]:
					pass
				else:
					print(counter - 1, ".", field)
				counter += 1

			choice = int(input("Enter choice: "))
			updateData = input("Enter {} to update: ".format(fields[choice]))
			connection.execute("UPDATE {} SET {} = '{}' WHERE {} = {} ".format(tableName, fields[choice], updateData, fields[0], data[0]))
			found = 1
			connection.commit()

	if found == 0:
		print("Data update error.")
	else:
		print("Data updated successfully.")

def deleteRecord():

	cursor = connection.execute("SELECT * FROM {}".format(tableName))
	found = 0
	dataToBeDeleted = int(input("Enter data to be deleted: "))
	for data in cursor:
		if data[0] == dataToBeDeleted:
			found = 1
			connection.execute("DELETE FROM {} WHERE {} = {}".format(tableName, fields[0], dataToBeDeleted))
			connection.commit()

	if found == 0:
		print("\nEntered data is wrong.")
	else:
		print("\nData Deleted successfully.")

def exitMenu():
	connection.close()
	print("\nThank You.")
	exit()


getFields()
while True:
	print("\n")
	with open(menuFileName) as f:
		menu = f.read()
		print(menu)
	[addRecord, readRecords, updateRecord, deleteRecord, exitMenu][int(input("Enter your choice: ")) - 1]()