import paho.mqtt.client as mqtt
from datetime import datetime
import signal
import sys

broker = "broker.emqx.io"
topic = "iot/lab/message"

def signal_handler(sig, frame):
    print("\nChương trình ngắt kết nối theo yêu cầu người dùng")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Hàm callback khi nhận được tin nhắn
def on_message(client, userdata, msg):
    current_time = datetime.now().strftime("%H:%M:%S")
    print("\n--- Nhan duoc message ---")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {msg.payload.decode('utf-8')}")
    print(f"Time: {current_time}")

client = mqtt.Client()
client.on_message = on_message

print(f"Dang ket noi den broker {broker}...")
client.connect(broker, 1883, 60)
client.subscribe(topic)

print(f"Da dang ky lang nghe topic: {topic}. Nhan Ctrl+C de thoat.")
client.loop_forever()