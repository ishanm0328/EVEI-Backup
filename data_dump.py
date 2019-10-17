#!/usr/bin/env python3
import serial
import serial_handler as sh

def data_dump(data):
    with open('data.csv', 'w') as o:
        for i in range(len(data)):
            o.write(','.join(map(str,list(data[i].values())))+'\n')