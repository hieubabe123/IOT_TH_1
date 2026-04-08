import paho.mqtt.client as mqtt
import json

broker = "broker.emqx.io"
cmd_topic = "iot/lab/light01/cmd"
status_topic = "iot/lab/light01/status"

current_status = "OFF"

def on_message(client, userdata, msg):
    global current_status
    command = msg.payload.decode('utf-8').strip().upper()
    print(f"\n[Device] Nhan duoc lenh: {command}")
    
    if command in ["ON", "OFF"]:
        current_status = command
        print(f"[Device] Chuyen trang thai thanh: {current_status}")

        response = {
            "device_id": "light01",
            "status": current_status
        } # [cite: 113]
        client.publish(status_topic, json.dumps(response))
        print(f"[Device] Da gui phan hoi: {response}")
    else:
        print("[Device] Lenh khong hop le!")

client = mqtt.Client()
client.on_message = on_message

client.connect(broker, 1883, 60)
client.subscribe(cmd_topic)

print(f"Smart Light dang hoat dong. Lang nghe lenh o topic: {cmd_topic}")
client.loop_forever()