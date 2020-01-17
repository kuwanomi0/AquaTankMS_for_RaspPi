#!/usr/bin/env python3
# hc_sr04.py : HC-SR04用距離取得プログラム
# coding: UTF-8
import RPi.GPIO as GPIO
import time

# TRIGとECHOのGPIO番号   
TRIG_PIN = 11
ECHO_PIN = 13
# 音速
SONIC_SPEED = 34000


# HIGH or LOWの時計測
def pulseIn(PIN, start=1, end=0):
    if start==0: end = 1
    t_start = 0
    t_end = 0
    # ECHO_PINがHIGHである時間を計測
    while GPIO.input(PIN) == end:
        t_start = time.time()
        
    while GPIO.input(PIN) == start:
        t_end = time.time()
    return t_end - t_start

# 距離計測
def get_distance():
    v=SONIC_SPEED
    # ピン番号をGPIOで指定
    GPIO.setmode(GPIO.BOARD)
    # TRIG_PINを出力, ECHO_PINを入力
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setwarnings(False)
    # TRIGピンを0.3[s]だけLOW
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.3)
    # TRIGピンを0.00001[s]だけ出力(超音波発射)        
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    # HIGHの時間計測
    t = pulseIn(ECHO_PIN)
    # 距離[cm] = 音速[cm/s] * 時間[s]/2
    distance = v * t/2
    # ピン設定解除
    GPIO.cleanup()

    return distance

#-- main --
def main():
    distance = get_distance()
    print(str(distance) + "cm")

if __name__ == '__main__' :
    main()