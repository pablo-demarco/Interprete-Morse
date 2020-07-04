import serial
import os

for puerto in range(0, 9):
    try:
        if 'nt' in os.name:
            arduino = serial.Serial(f'COM{puerto}', 9600)
        else:
            arduino = serial.Serial(f'/dev/ttyACM{puerto}', 9600)
    except Exception as e:
        pass

    
while True:
    s = str(input()).lower().encode()
    arduino.write(s)

arduino.close()