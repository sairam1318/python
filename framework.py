# CRUD Operation using sqlite3
import sqlite3
dataBaseName = "flow.db"
tableName = "FLOW"
menuFileName = "menu.cfg"

connection = sqlite3.connect(dataBaseName) 
fields = []

def getFields():

	metadata = connection.execute("PRAGMA TABLE_INFO({})".format(tableName))
	for field in metadata:
		fields.append(field[1])
	print(fields)
	

def addRecord():

	values = ""
	for field in fields:
		storeData = input("\nEnter the " + field + ": ")
		if field == fields[-1]:
			values += "\'" + storeData + "\' "
		else:
			values += "\'" + storeData + "\', "

	connection.execute("INSERT INTO {} VALUES ({})".format(tableName, values))
	connection.commit()

def readRecords():

	cursor = connection.execute("SELECT * FROM {}".format(tableName))

	for data in cursor:
		print("\n")
		for item in data:
			print(item, end = " ")


def updateRecord():

	dataToBeUpdated = input("Enter " + fields[0].lower() + "to be updated: ")

	cursor = connection.execute("SELECT * FROM {}".format(tableName))
	found = 0
	for data in cursor:
		if data[0] == dataToBeUpdated:
			
			print("Chose any one of the following to update: ")
			counter = 1
			for field in fields:
				if field == fields[0]:
					pass
				else:
					print(counter - 1, ".", field)
				counter += 1

			choice = int(input("Enter choice: "))
			updateData = input("Enter {} to update: ".format(fields[choice]))				
			connection.execute("UPDATE {} SET {} = '{}' WHERE {} = '{}' ".format(tableName, fields[choice], updateData, fields[0], data[0]))
			found = 1
			connection.commit()

	if found == 0:
		print("No such id ")
	else:
		print("Updated Successfully.")


def deleteRecord():
	cursor = connection.execute("SELECT * FROM {}".format(tableName))
	found = 0
	dataToBeDeleted = input("Enter data to be deleted: ")
	for data in cursor:
		if data[0] == dataToBeDeleted:
			found = 1
			connection.execute("DELETE FROM {} WHERE {} = '{}'".format(tableName, fields[0], dataToBeDeleted))
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