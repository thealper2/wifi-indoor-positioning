import network
import urequests
import json

SSID = ""
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)

wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    pass

print("Connected to WiFi")
print("IFCONFIG: ", wifi.ifconfig())

signal_strength = wifi.status('rssi')

url = 'http://172.22.58.201:5000/get_room'
payload = {'signal': signal_strength}
headers = {'Content-Type': 'application/json'}

response = urequests.post(url, json=payload, headers=headers)
prediction = response.json()

print("Predicted Location:", prediction)

response.close()
wifi.disconnect()
