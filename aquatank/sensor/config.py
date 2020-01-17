#!/usr/bin/env python3
# sensor_config.py : 各センサー設定値
# coding: UTF-8

# DS18B20 (Temperature Sensor)
DS18B20_SENSOR_ID = '28-031397799b9b'
SENSOR_W1_SLAVE = '/sys/bus/w1/devices/' + DS18B20_SENSOR_ID + '/w1_slave'

# HC-SR04 (Ultraonic Sensor)
HC_SR04_TRIG_PIN = 11
HC_SR04_ECHO_PIN = 13
HC_SR04_ECHO_SONIC_SPEED = 34000

# DHT22 (Humidity and Temperature Sensor)
DHT22_GPIO = 22