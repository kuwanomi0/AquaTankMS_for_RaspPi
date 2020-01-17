import datetime

from hc_sr04 import *


#-- main --
def main():
    # 水温取得
    waterTemp = 0
    # 水位用距離取得
    disValue = get_distance()
    # 室内温湿度取得
    roomHum, roomTemp = [0, 0]

    date_now = datetime.datetime.now(datetime.timezone.utc) 
    resultStr = '{}: W:{}, D:{}, T:{}, H:{}'.format(date_now.isoformat(),
        round(waterTemp, 1),
        round(disValue, 1),
        round(roomTemp, 1),
        round(roomHum, 1))
    print(resultStr)

if __name__ == '__main__' :
    main()