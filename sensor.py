import paho.mqtt.client as mqtt
import serial

ser=serial.Serial('/dev/ttyACM0',9600)
broker_addr = '114.33.252.156'
client = mqtt.Client("sensor1")

while True: 
	readedText = ser.readline()
	client.connect(broker_addr)
	client.publish("Sensor/Charlie/tmp_water",readedText) # 輸入格式:溫度 水位
	print(readedText)
ser.close()
