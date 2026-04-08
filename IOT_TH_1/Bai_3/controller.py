import paho.mqtt.client as mqtt
import json
import time

broker = "broker.emqx.io"
cmd_topic = "iot/lab/light01/cmd"
status_topic = "iot/lab/light01/status"

def on_message(client, userdata, msg):
    print("\nTrang thai nhan duoc:")
    print(msg.payload.decode('utf-8'))

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, 1883, 60)
client.subscribe(status_topic)

client.loop_start() 

time.sleep(1)
print("--- He Thong Dieu Khien Den ---")
while True:
    cmd = input("Nhap lenh (ON/OFF/EXIT): ").strip().upper()
    
    if cmd == 'EXIT':
        print("Ket thuc chuong trinh.")
        break
    elif cmd in ['ON', 'OFF']:
        client.publish(cmd_topic, cmd)
        print(f"Da gui lenh {cmd} toi light01") 
        time.sleep(0.5)
    else:
        print("Loi: Chi chap nhan lenh ON hoac OFF.")

client.loop_stop()
client.disconnect()