import paho.mqtt.client as mqtt
import json
import time
import random

broker = "broker.emqx.io"
topic = "iot/lab/sensor01/data"

client = mqtt.Client()
client.connect(broker, 1883, 60)

print("Bat dau gui du lieu cam bien (3 giay / lan)... Nhan Ctrl+C de thoat.")

try:
    while True:
        temp = round(random.uniform(25.0, 38.0), 1) 
        hum = round(random.uniform(30.0, 70.0), 1)
        
        data = {
            "device_id": "sensor01",
            "temperature": temp,
            "humidity": hum
        }
        
        payload = json.dumps(data) 
        client.publish(topic, payload)

        print(f"Da gui: {payload}")
        time.sleep(3)
except KeyboardInterrupt:
    print("Da dung mo phong cam bien.")