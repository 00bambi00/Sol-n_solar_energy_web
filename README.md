# Sol-n_solar_energy_web

โปรเจคนี้เป็นเว็บแอปที่ให้ผู้ใช้ "พิมพ์ชื่อเมือง" แล้วระบบจะแสดง:
- พิกัด (Latitude, Longitude)
- ค่า Solar Irradiance (W/m²) ของวันนี้
- พลังงานไฟฟ้าที่ประมาณจะผลิตได้ (kWh)
- พร้อมกราฟแท่งแสดงค่า Irradiance

## โครงสร้างโปรเจค

solar_web_project/
│
├── app.py
├── city_to_coords.py
├── fetch_solar_data.py
├── solar_energy_predict.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
└── README.md

## วิธีใช้งาน

1. คลิกเข้าโฟลเดอร์โปรเจค
   ```bash
   cd solar_web_project
2. สร้างและเปิดใช้งาน virtual environment
- macOS/Linux: python3 -m venv venv
               source venv/bin/activate
3. ติดตั้ง dependencies: pip install -r requirements.txt
4. รันเว็บเซิร์ฟเวอร์: python app.py
5. เปิดเว็บเบราว์เซอร์ไปที่: http://127.0.0.1:5000
6. พิมพ์ชื่อเมืองในช่องค้นหา แล้วกด “ค้นหา” ระบบจะแสดงผลพร้อมกราฟ

# 


