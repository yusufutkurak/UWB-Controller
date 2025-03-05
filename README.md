# UWB-Controller

Bu proje, **ESP32** ile **BNO055 IMU** kalibrasyonu ve veri alma işlemlerini içerir. Ayrıca, **DWM1001-DEV** modülü ile UWB (Ultra-Wideband) sensörleri üzerinden konum verisi almayı sağlar.

## BNO055 IMU Kullanımı

- **Arduino IDE** kullanılarak ESP32'ye kod yüklenir.
- **Seri Monitör** üzerinden veriler okunabilir.
- **Kalibrasyon durumu:** 
  - Kalibrasyon tamamlandığında, **ESP32'nin 7. pinine bağlı LED yanar**.

## DWM1001-DEV Kullanımı

1. **Sensörleri USB ile bilgisayara bağlayın.**
2. Terminali açın ve aşağıdaki komut ile bağlı portları görüntüleyin:

    ```sh
    ls /dev/cu.*
    ```

    **Örnek Çıktı:**
    ![Bağlı portlar](https://github.com/user-attachments/assets/90a5d280-39b1-4cbd-b6be-4e46b90251e7)

3. **DWM1001 terminaline erişmek için şu komutu çalıştırın:**

    ```sh
    screen /dev/<PORT_ADI> 115200
    ```

    - **Not:** `<PORT_ADI>` yerine, `ls /dev/cu.*` komutuyla bulduğunuz port adını yazmalısınız.
    - Açılan terminal ekranında **2 kez Enter** tuşuna basarak terminali etkinleştirin.

    **Terminal Görünümü:**
    ![DWM1001 Terminali](https://github.com/user-attachments/assets/4a3ec7f7-f7f0-4f47-860d-d6ea19d96c37)

4. **Sistem bilgilerini görüntülemek için şu komutu kullanabilirsiniz:**

    ```sh
    si
    ```

    **Örnek Çıktı:**
    ![Sistem Bilgisi](https://github.com/user-attachments/assets/026120e9-d7e5-4bf9-a9e0-cd8e7d94b383)

5. **Konum verisi almak için aşağıdaki komutları kullanabilirsiniz:**

    ```sh
    les
    an
    ```

    **Örnek Çıktı:**
    ![Konum Verisi](https://github.com/user-attachments/assets/959c364c-704a-47a1-8739-789de2988d80)

## Python ile Veri Okuma

1. **Bağlantıyı kurduktan sonra** `main.py` dosyasını çalıştırarak verilere Python üzerinden erişebilirsiniz:

    ```sh
    python main.py
    ```

    **Örnek Çıktı:**
    ![Python Veri Okuma](https://github.com/user-attachments/assets/d52fb6c4-2a7e-4ba4-9e91-7bbdd7a3e4cb)

## Hesaplama mantığı

![WhatsApp Image 2025-03-05 at 16 00 59](https://github.com/user-attachments/assets/79464fec-d253-4942-bee2-ff738814c21c)

![WhatsApp Image 2025-03-05 at 16 21 33](https://github.com/user-attachments/assets/47911923-f27c-4c0d-9eb0-f121dc5f8ce7)


## Ek Belgeler

- **Detaylı komut listesi ve açıklamalar** için `docs` klasöründe bulunan PDF dökümanını inceleyebilirsiniz.
