import paho.mqtt.client as mqtt
import json

broker = "broker.emqx.io"
topic = "iot/lab/sensor01/data"

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode('utf-8'))
        temp = payload.get('temperature', 0)
        hum = payload.get('humidity', 0)
        
        print("-" * 30)
        print(f"Device: {payload.get('device_id', 'unknown')}")
        print(f"Temperature: {temp} C")
        print(f"Humidity: {hum} %")
        
        if temp > 35:
            print("CANH BAO: Nhiet do cao")
        if hum < 40: # [cite: 78]
            print("CANH BAO: Do am thap")
            
    except json.JSONDecodeError:
        print("Loi: Du lieu nhan duoc khong phai format JSON.")

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, 1883, 60)
client.subscribe(topic)

print(f"Dang lang nghe du lieu cam bien tai topic: {topic}...")
client.loop_forever()