#!/usr/bin/env python3
# dht20.py : DHT20用温度・湿度取得プログラム
# coding: UTF-8

# https://github.com/freedom27/MyPyDHT
import MyPyDHT

GPIO = 22


# 温度・湿度取得
def get_humidity_temperature():
    try:
        roomHum, roomTemp = MyPyDHT.sensor_read(MyPyDHT.Sensor.DHT22, GPIO)
    except MyPyDHT.DHTException:
        roomHum = 0.0
        roomTemp = 0.0

    return roomHum, roomTemp

#-- main --
def main():
    humidity, temperature = get_humidity_temperature()
    print(str(temperature) + "℃")
    print(str(humidity) + "%")

if __name__ == '__main__' :
    main()