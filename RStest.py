import serial, time, struct

  
ser = serial.Serial()
ser.port = "/dev/ttyUSB0"

# 9600, 8, N, 1
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
  
ser.timeout = 0.5          #non-block read 0.5s
ser.writeTimeout = 0.5     #timeout for write 0.5s
ser.xonxoff = False    #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False     #disable hardware (DSR/DTR) flow control

try: 
    ser.open()
except Exception as ex:
    print ("open serial port error " + str(ex))
    exit()
  
if ser.isOpen():
  
    try:
        ser.flushInput() #flush input buffer
        ser.flushOutput() #flush output buffer
                 
        #write 8 byte data
        ser.write([01, 03, 00, 00, 00, 01, 132, 10])
        print("write 8 byte data:01, 03, 00, 00, 00, 01, 84, 0A")
  
        time.sleep(0.5)  #wait 0.5s
  
        #read 8 byte data
        response = ser.read(7)
        print("read 8 byte data:")
        for i in response:
                print(hex(ord(i)))
  
        ser.close()
    except Exception as e1:
        print ("communicating error " + str(e1))
  
else:
    print ("open serial port error")
