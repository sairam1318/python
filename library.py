dataFileName = "data.dat"
menuFileName = "menu.cfg"
fields = ["Id", "Name", "Author"]
gData = []

def create():
	with open(dataFileName, "w") as dataFileObject:
		dataList = []
		for field in fields:
			dataList.append(input("Enter " + field + ": "))
		gData.append(dataList)
		dataFileObject.write(str(gData))	

def readData():
	with open(dataFileName) as dataFileObject:
		for field in fields:
			print(field, end = " ")
		record = dataFileObject.read()
		temp = eval(record)
		for items in temp:
			print("")
			for item in items:
				print(item, end = " ")

def exitMenu():
	print("\nThanks!")
	exit()

def menu():
	with open(menuFileName) as menuFileObject:
		menuLine = menuFileObject.read()
		print("\n")
		print(menuLine, end = " ")

def search():
	dataToBeSearched = input("\nEnter ID to search: ")
	for row in gData:
		for coloumn in row:
			if dataToBeSearched == coloumn:
				print(row)
				break;

def update():
	dataToBeUpdated = input("\nEnter ID to update: ")
	rowCount = 0;
	coloumnCount = 0;
	for row in gData:
		rowCount += 1;
		for coloumn in row:
			coloumnCount += 1;
			if dataToBeUpdated == coloumn:
				updateName = input("\nEnter updated Name: ")
				updateAuthor = input("\nEnter updated Author: ")
				updateList = [dataToBeUpdated, updateName, updateAuthor]
				gData[rowCount - 1] = updateList

	with open(dataFileName, "w") as dataFileObject:
		dataFileObject.write(str(gData))
				


def storeDataInList():
	with open(dataFileName) as dataFileObject:
		temp = dataFileObject.read()
		listed = eval(temp)
		for row in listed:
			gData.append(row)



storeDataInList()		
while True:
	menu()
	[create, readData, search, update, exitMenu][int(input("\nEnter your choice: ")) - 1]()