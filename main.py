import serial
import os
import time

for puerto in range(0, 9):
    try:
        if 'nt' in os.name:
            arduino = serial.Serial(f'COM{puerto}', 9600)
        else:
            arduino = serial.Serial(f'/dev/ttyACM{puerto}', 9600)
    except Exception as e:
        pass

    
while True:
    s = str(input()).lower()#.encode()
    if ':q' in s:
        break
    if ':c' in s:
        ss = s.split(':')
        s = ss[0]
        m = ss[1][1:]
    else:
        m = 1
    print (s, m)
    for i in range(int(m)):
        arduino.write(s.encode())
        time.sleep(5)

arduino.close()