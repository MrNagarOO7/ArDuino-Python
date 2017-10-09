import serial

port = "COM3"
pin = serial.Serial(port,9600)

no = "NO"

print("L : LOW H : HIGH E : Exit")
while(no != "E"):
    no=input("Enter Choice:").upper()
    if(no == "L"):
            print('L')
            pin.write(str.encode("L",'utf-8'))
    elif(no == "H"):
            pin.write(str.encode("H",'utf-8'))
