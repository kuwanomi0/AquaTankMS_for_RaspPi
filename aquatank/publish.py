#!/usr/bin/env python3
# publish.py : パブリッシュ処理用プログラム
# coding: UTF-8
import datetime
import time
import paho.mqtt.client as mqtt

import sensor
from variables import *

#-- MQTT 定義 ----
# ブローカーに接続できたときの処理
def on_connect(client, userdata, flag, rc):
    print('Connected with result code ' + str(rc))
    
# ブローカーが切断されたときの処理
def on_disconnect(client, userdata, flag, rc):
    if rc != 0 :
        print('Unexpected disconnection.')

# publishが完了したときの処理
def on_publish(client, userdata, mid):
    print("publish: {0}".format(mid))

#-- Main ----
# print("START: " + str(__file__))
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
def main():
    print('connected to: ', broker_url)
    interval_sec = 5
    client.connect(broker_url, 1883, 60)
    client.loop_start()

    waterTemp = 0.0
    disValue = 0.0
    roomTemp = 0.0
    roomHum = 0.0

    try:
        while True:
            start_timing = datetime.datetime.now()
            # print(start_timing.strftime('%H:%M:%S.%f'))

            roomHumT = roomHum
            roomTempT = roomTemp
            # 水温取得
            waterTemp, disValue, roomHum, roomTemp = sensor.get_value()

            if str(roomHum) == '0.0' :
                roomHum = roomHumT
            if str(roomTemp) == '0.0' :
                roomTemp = roomTempT

            date_now = datetime.datetime.now(datetime.timezone.utc) 
            resultStr = '{}: W:{}, D:{}, T:{}, H:{}'.format(date_now.isoformat(),
                round(waterTemp, 1),
                round(disValue, 1),
                round(roomTemp, 1),
                round(roomHum, 1))
            print(resultStr)
            client.publish(sensor_topic, str(resultStr))

            end_timing = datetime.datetime.now()
            time_delta_sec = (end_timing - start_timing).total_seconds()
            sleep_sec = interval_sec - time_delta_sec - 0.00397

            time.sleep(max(sleep_sec, 0))

    except(KeyboardInterrupt, SystemExit):
        print('SIGINTを検知')

    print("END.")

if __name__ == "__main__":
    main()