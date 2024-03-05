'''
import serial

port = "COM3"
baudrate = 9600

try:
    ser = serial.Serial(port, baudrate)
except serial.SerialException as e:
    print(f"Lỗi mở cổng COM: {e}")
    exit()

data = int.to_bytes(12, byteorder='big')

try:
    ser.write(data)
except serial.SerialException as e:
    print(f"Lỗi gửi dữ liệu: {e}")
    exit()

if ser.write(data) == len(data):
    print("Dữ liệu đã được gửi thành công!")
else:
    print("Lỗi gửi dữ liệu!")

# Đọc dữ liệu từ cổng COM
data = ser.read(20)
print(f"Dữ liệu nhận được: {data}")

ser.close()
'''
import serial
import time

port = "COM3"
baudrate = 9600

try:
    ser = serial.Serial(port, baudrate)
except serial.SerialException as e:
    print(f"Lỗi mở cổng COM: {e}")
    exit()

data = b"x: 10, y: 250"

while(True):
    try:
        ser.write(data)
    except serial.SerialException as e:
        print(f"Lỗi gửi dữ liệu: {e}")
        exit()

    if ser.write(data) == len(data):
        print("Dữ liệu đã được gửi thành công!")
    else:
        print("Lỗi gửi dữ liệu!")
    time.sleep(1)
    
    

# Đọc dữ liệu từ cổng COM
#data = ser.read(10)
#print(f"Dữ liệu nhận được: {data.decode()}")

ser.close()
