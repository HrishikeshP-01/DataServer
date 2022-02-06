from csv import writer

def MakeData(filename, n):
    currentTime=0
    delayTime=500

    file=open(filename, "a")
    writer_object=writer(file)

    rowData = addCols()
    writer_object.writerow(rowData)

    for i in range(n):
        rowData=[]
        rowData.append(str(currentTime))
        rowData.append(generateFlexData())
        rowData.append(generateTempData())
        rowData.append(generatePulseData())
        writer_object.writerow(rowData)
        currentTime+=delayTime/1000
    file.close()

def generateFlexData():
    return "30"

def generateTempData():
    return "90"

def generatePulseData():
    return "78"

def addCols():
    rowData=["Time","Flex","Temp","Pulse"]
    return rowData

def main():
    filename = input("Enter filename with .csv: ")
    n = int(input("Enter no: of data entries: "))
    MakeData(filename,n)

if __name__ == "__main__":
    main()