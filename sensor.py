import paho.mqtt.client as mqtt
import serial

ser=serial.Serial('/dev/ttyUSB0',9600)
broker_addr = '114.33.252.156'
client = mqtt.Client("sensor1")

while True: 
	readedText = ser.readline()
	client.connect(broker_addr)
	client.publish("Sensor/Charlie/temp_water",readedText) # Input format : TEMPERATURE xx.xx\n
	print(readedText)
ser.close()
