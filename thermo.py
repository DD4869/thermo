import Adafruit_DHT as DHT
import requests

##type of sensor
SENSOR_TYPE = DHT.DHT22

##GPI0 port number
DHT_GPIO = 4

## start mesurement
h,t = DHT.read_retry(SENSOR_TYPE, DHT_GPIO)
Temp = "Temp is {0:0.1f} ℃" .format(t)
Humidity = "Humidity is = {0:0.1f} %" .format(h)
message = "\n" + Temp + "\n" + Humidity
print (message)

url = "https://notify-api.line.me/api/notify"
token = "SuAv0caf6HNSHymnOkJjSMP3ntFEJgIfjdjhng2Sn0F"
headers = {"Authorization" : "Bearer "+ token}
payload = {"message" : message}
r = requests.post(url, headers = headers, params = payload)