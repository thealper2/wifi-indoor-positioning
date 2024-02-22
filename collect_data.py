import network
import time
import machine
from machine import Pin

p4 = Pin(2, Pin.OUT)

SSID = ""
PASSWORD = ""

wifi = network.WLAN(network.STA_IF)

wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    pass

print("Connected to WiFi")

def scan_wifi():
    signal_strength = wifi.status('rssi')
    print("Signal strength:", signal_strength, "dBm")
    
    with open("living_room.txt", "a") as file:
        file.write(str(signal_strength) + "\n")

i = 0

while i < 100:
    print("Scanning WiFi networks...")
    scan_wifi()
    i += 1
    time.sleep(0.5)

p4.on()
