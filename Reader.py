import serial
from csv import writer

arduino_port = "COM7" # serial port of Arduino
baud = 9600 # arduino uno runs at 9600 baud
fileName = "analog-data.csv" # name of CSV file generated

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port: "+arduino_port)
file=open(fileName,"a")
print("Created File")

samples=10
print_labels=False
line=0 # start at 0 because our header is 0
while line<=samples:
    # incoming = ser.read(9999)
    # if len(incoming) > 0:
    if print_labels:
        if line==0:
            print("Printing Column Headers")
        else:
            print("Line"+str(line)+": write....")

    # display the data to the terminal
    getData=ser.readline()
    data=getData[0:][:-2].decode("utf-8") 
    print(data)
    rowData = data.split(' ')

    # add the data to the file
    file=open(fileName,"a") # append the data to the file
    writer_object=writer(file)
    writer_object.writerow(rowData) # write data with a new line
    line=line+1
print("Data collection complete!")
#close out the file
file.close()