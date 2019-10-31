import csv
import sys
from time import sleep

def format(rpm, analog_a, analog_b, digital, energy, gyro_x, gyro_y, gyro_z):
    return 'RM{: <5}A{:.1f}B{:.1f}{:s}\nE{: <6}{:<+3}{:<+3}{:<+3}\n'.format(
            rpm, analog_a, analog_b, digital, energy, gyro_x, gyro_y, gyro_z)

with open(sys.argv[1]) as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    next(reader)
    next(reader)
    for row in reader:
        digital = ' '
        if row[10] == 1:
            digital = 'D'
        rpm = int(float(row[7]))
        analog_a = float(row[5])
        analog_b = float(row[6])
        energy = int(float(row[4])) if row[4].strip() else 0
        gyro_x = int(float(row[8]))
        gyro_y = int(float(row[9]))
        gyro_z = int(float(row[10]))
        s = format(rpm, analog_a, analog_b, digital, energy, gyro_x, gyro_y, gyro_z)
        print(s)
        sleep(1)
