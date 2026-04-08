# Bài thực hành: Lập trình Python với MQTT

## Broker sử dụng
- **Họ và tên**: `Đặng Minh Hiếu`  
- **MSV**: `B21DCAT087`

## Broker sử dụng
- **Broker**: `broker.emqx.io`  
- **Port**: `1883`

---

## Cài đặt thư viện

```bash
pip install paho-mqtt
```

---

## Cách chạy từng chương trình

### Bài 1 – Gửi và nhận thông điệp cơ bản

#### Folder Bai_1
Chạy 2 Terminal:

**Terminal 1 – Subscriber:**
```bash
python subscriber.py
```

![alt text](./Image_Cap/Bai_1/1_Subscriber_Run.png)

**Terminal 2 – Publisher:**
```bash
python publisher_bai1.py
```

![alt text](./Image_Cap/Bai_1/1_Publisher_Run.png)

**KẾT QUẢ**

**Publisher:** (Có thể gửi nhiều lần)

![alt text](./Image_Cap/Bai_1/1_Publisher_Send.png)

**Subscriber:** (Nhận được nhiều tin nhắn gửi qua từ Publisher)

![alt text](./Image_Cap/Bai_1/1_Subcriber_Receive.png)

**Subscriber:** (Dừng chương trình bằng Ctrl + C)

![alt text](./Image_Cap/Bai_1/1_Subcriber_Stop.png)

---


### Bài 2 – Mô phỏng cảm biến nhiệt độ & độ ẩm

Chạy 2 terminal:

**Terminal 1 – Monitor Subscriber:**
```bash
python monitor_subscriber.py
```

![alt text](./Image_Cap/Bai_2/2_Monitor_Subscriber_Run.png)

**Terminal 2 – Sensor Publisher:**
```bash
python sensor_publisher.py
```

![alt text](./Image_Cap/Bai_2/2_Sensor_Publisher_Run.png)

**KẾT QUẢ**

**Sensor Publisher:** (Hướng 1 Sensor)

![alt text](./Image_Cap/Bai_2/2_Sensor_Publisher_Send.png)

**Monitor Subscriber:** (Có cảnh báo nhiệt độ cao, độ ẩm thấp)

![alt text](./Image_Cap/Bai_2/2_Monitor_Subscriber_Received.png)

---

### Bài 3 – Hệ thống điều khiển đèn thông minh

Chạy 2 Terminal:

**Terminal 1 – Smart Light Device:**
```bash
python device.py
```

![alt text](./Image_Cap/Bai_3/3_Device_Run.png)

**Terminal 2 – Controller App:**
```bash
python controller.py
```

![alt text](./Image_Cap/Bai_3/3_Controller_Run.png)

Nhập lệnh vào Terminal Controller:
- `ON` — bật đèn / `OFF` — tắt đèn

![alt text](./Image_Cap/Bai_3/3_Controller_OnOff.png)

Kết quả hiển thị Terminal Device

![alt text](./Image_Cap/Bai_3/3_Device_OnOff.png)

- Nhập khác `ON` / `OFF`
![alt text](./Image_Cap/Bai_3/3_Controller_Error.png)

- `EXIT` — Thoát chương trình

![alt text](./Image_Cap/Bai_3/3_Controller_Exit.png)

---

