#!/usr/bin/env python3
# ds18b20.py : DS18B20用温度取得プログラム
# coding: UTF-8
import subprocess

DS18B20_SENSOR_ID = '28-031397799b9b'
SENSOR_W1_SLAVE = '/sys/bus/w1/devices/' + DS18B20_SENSOR_ID + '/w1_slave'

# 温度取得
def get_temperature():
    res = subprocess.check_output(['cat', SENSOR_W1_SLAVE]).decode('utf-8')
    temp_val = res.split('=')
    temp_val = float(temp_val[-1]) / 1000
    return temp_val

#-- main --
def main():
    temperature = get_temperature()
    print(str(temperature) + "℃")

if __name__ == '__main__' :
    main()