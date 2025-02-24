import serial
import time

PORT = "/dev/cu.usbmodem0007602026701"  # Mac için doğru portu kullan
BAUDRATE = 115200  # Gerekirse 921600 veya 460800 gibi farklı değerleri dene

try:
    # 🔹 Seri portu aç
    ser = serial.Serial(
        PORT,
        BAUDRATE,
        timeout=1,
        write_timeout=1,
        rtscts=False,
        dsrdtr=False
    )

    print("✅ DWM1001'e bağlanıldı. UART buffer temizleniyor...")
    
    # 🔹 Önce buffer'ı temizle ve eski verileri at
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(1)

    # 🔹 İlk birkaç satırı görmezden gel (çünkü çöp veri gelebilir)
    for _ in range(3):
        ser.readline()

    # 🔹 `les` komutu gönder ve bekle
    print("🔹 `les` komutu gönderiliyor...")
    ser.write(b"les\r\n")
    time.sleep(0.5)

    # 🔹 Gelen veriyi sürekli oku
    while True:
        line = ser.readline().decode("latin-1", errors="ignore").strip()
        if line:
            print("📡 UWB Veri:", line)

except serial.SerialException as e:
    print("❌ Seri porta bağlanılamadı:", str(e))
except KeyboardInterrupt:
    print("\nÇıkış yapılıyor...")
    ser.close()
