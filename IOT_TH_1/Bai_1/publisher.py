import paho.mqtt.client as mqtt

# ------ Cấu hình MQTT ------
broker = "broker.emqx.io"
port = 1883
topic = "iot/lab/message"

# ------ Thông tin Sinh viên ------
name = "Đặng Minh Hiếu"
msv = "B21DCAT087"
content = "Xin chào từ client Python MQTT "

# ------ Kết nối MQTT ------
client = mqtt.Client()
client.connect(broker, port, 60) # [cite: 26]

print("--- MQTT Publisher ---")
print("Nhap 'exit' de thoat.")
while True:
    msg_input = input("Nhap tin nhan (Enter de gui topic mac dinh): ")
    if msg_input == "":
        payload = f"{content} -{msv} - {name}"
    else:
        payload = msg_input
    client.publish(topic, payload)