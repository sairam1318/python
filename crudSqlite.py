# CRUD Operation using sqlite3
import sqlite3
dataBaseName = "data.db"
menuFileName = "menu.cfg"

connection = sqlite3.connect(dataBaseName) 

def Table():
	connection.execute(
		''' CREATE TABLE BANK_CUSTOMER_DETAILS
		(ACCOUNT_NUM INT PRIMARY KEY NOT NULL,
		NAME TEXT NOT NULL,
		MOBILE_NUM TEXT NOT NULL,
		MAIL_ID TEXT

		);
		'''
		)

def addRecord():

	accountNumber = input("Enter the Account Number: ")
	name = input("Enter Name: ")
	mobileNumber = input("Enter the Mobile Number: ")
	mail = input("Enter the mail Id: ")

	connection.execute("INSERT INTO BANK_CUSTOMER_DETAILS VALUES(?, ?, ?, ?)", (accountNumber, name, mobileNumber, mail))

	connection.commit()

def readRecords():

	cursor = connection.execute("SELECT * FROM BANK_CUSTOMER_DETAILS")

	for data in cursor:
		print(data[0], data[1], data[2], data[3])
		
def updateRecord():
	
	cursor = connection.execute("SELECT * FROM BANK_CUSTOMER_DETAILS")

	dataToUpdate = input("Enter record ID to be updated: ")

	for data in cursor:
		if str(data[0]) == dataToUpdate:
			print("Choose an option to update: \n1.Name\n2.Mobile Number\n3.Mail\n")
			choice = int(input())
			if choice == 1:
				name = input("Enter the updated Name: ")
				connection.execute("UPDATE BANK_CUSTOMER_DETAILS SET NAME = ? WHERE ACCOUNT_NUM = ?", (name, data[0]))

			elif choice == 2:
				mobileNumber = input("Enter the updated mobile number: ")
				connection.execute("UPDATE BANK_CUSTOMER_DETAILS SET MOBILE_NUM = ? WHERE ACCOUNT_NUM = ?", (mobileNumber, data[0]) )
			elif choice == 3:
				email = input("Enter the email: ")
				connection.execute("UPDATE BANK_CUSTOMER_DETAILS SET MAIL_ID = ? WHERE ACCOUNT_NUM = ? ", (email, data[0]))
			else:
				break;

		connection.commit()



def deleteRecord():
	recordToBeDeleted = input("Enter data to be deleted: ")
	cursor = connection.execute("SELECT * FROM BANK_CUSTOMER_DETAILS")
	for data in cursor:
		if str(data[0]) == recordToBeDeleted:
			cursor.execute("DELETE from BANK_CUSTOMER_DETAILS where ACCOUNT_NUM = ?", (data[0],))
	
	connection.commit()


def exitMenu():
	connection.close()
	exit()


while True:
	with open(menuFileName) as f:
		data = f.read()
		print(data)
	[addRecord, readRecords, updateRecord, deleteRecord, exitMenu][int(input("Enter your choice: ")) - 1]()
