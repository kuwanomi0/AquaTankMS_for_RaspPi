import datetime
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
print("START: " + str(__file__))
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
print('connected to: ', broker_url)
client.connect(broker_url, 1883, 60)
client.loop_start()

try:
    while True:
        # 水温取得
        waterTemp, disValue, roomHum, roomTemp = sensor.get_value()

        date_now = datetime.datetime.now(datetime.timezone.utc) 
        resultStr = '{}: W:{}, D:{}, T:{}, H:{}'.format(date_now.isoformat(),
            round(waterTemp, 1),
            round(disValue, 1),
            round(roomTemp, 1),
            round(roomHum, 1))
        client.publish(sensor_topic, str(resultStr))

except(KeyboardInterrupt, SystemExit):
    print('SIGINTを検知')

print("END.")