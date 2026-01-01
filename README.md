⚠️ YASAL UYARI (DISCLAIMER)

Bu araç SADECE EĞİTİM VE SİBER GÜVENLİK FARKINDALIĞI amacıyla paylaşılmıştır. Bu kodun izinsiz veya etik dışı kullanımı yasal sorumluluk doğurabilir. Geliştirici, aracın kötüye kullanımından doğacak hiçbir zarardan sorumlu tutulamaz. Lütfen sadece kendi cihazlarınızda veya izin aldığınız sistemlerde test ediniz.Ve cloudflare ile internete açtıktan kısa süre sonra lütfen kapatınız 






🚀 Kullanım ve Kurulum Rehberi (Canlı Erişim)

Bu aracı yerel ağınızda veya bir sunucu üzerinde test etmek için aşağıdaki adımları takip edebilirsiniz:
1. Hazırlık ve Kurulum

Bilgisayarınızda Python 3.x yüklü olduğundan emin olun. Ardından projeyi klonlayın ve gerekli kütüphaneleri yükleyin:

    Projeyi İndirin: git clone https://github.com/kullaniciadin/pip-analiz-poc.git

    Dizine Geçin: cd pip-analiz-poc

    Bağımlılıkları Yükleyin: pip install flask flask-socketio

2. Sunucuyu Başlatma

Sunucuyu kendi bilgisayarınızda veya dış dünyaya açık bir tünel (Ngrok, Cloudflare vb.) üzerinden başlatın:

    Komut: python app.py

    Erişim: Sunucu başladığında tarayıcıda http://localhost:5000 (veya tünel adresiniz) üzerinden erişilebilir olacaktır.

3. Uygulama ve Test (Adım Adım)

Zafiyetin analizini bir Android cihaz üzerinde şu şekilde gerçekleştirebilirsiniz:

    Bağlantı: Android cihazınızdaki Chrome tarayıcıyı açın ve sunucu adresine gidin.

    İzin: Sayfada bulunan "Analizi Başlat" butonuna tıklayın ve kamera erişim isteğine "İzin Ver" yanıtını seçin.

    PiP Aktivasyonu: Kamera görüntüsü geldikten sonra cihazın Orta Tuşuna (Home) basarak ana ekrana dönün.

    Gözlem: Ekranın sağ alt köşesinde küçük bir video kutusunun (Picture-in-Picture) oluştuğunu göreceksiniz.

    Sonuç: Tarayıcı arka planda olmasına rağmen, kamera görüntüsünün sunucuya akmaya devam ettiğini panelinizden doğrulayın.

4. Platform Farklılıkları

Aynı testi bir iOS/iPadOS cihazda denediğinizde, ana ekrana geçtiğiniz anda Apple'ın güvenlik politikaları gereği kameranın otomatik olarak kapandığını ve görüntünün kesildiğini gözlemleyebilirsiniz.  






🛠️ Kurulum ve Kullanım Kılavuzu (Video Kayıt Destekli yani Video Kaydı)

Bu proje, modern web teknolojilerinin (PiP API ve MediaStream) güvenlik sınırlarını test etmek için tasarlanmıştır. Aşağıdaki adımları takip ederek siber güvenlik laboratuvarınızı kurabilirsiniz.
1️⃣ Tek Tıkla Kurulum

Bilgisayarınızda veya telefonunuzda (Termux) terminali açın. Hazırladığım setup.sh betiği tüm kütüphaneleri ve klasörleri sizin için hazırlar:
Bash

# Betiğe çalıştırma izni verin
chmod +x setup.sh

# Kurulumu başlatın
./setup.sh

Bu işlem; flask kütüphanesini kurar ve videoların kaydedileceği captured_videos klasörünü otomatik olarak oluşturur.

2️⃣ Uygulamayı Başlatma

Kurulum bittikten sonra ana sunucuyu çalıştırın:
Bash

python app.py

Sunucunuz varsayılan olarak 5000 portunda yayına başlar.
3️⃣ Test ve Uygulama Adımları

    Bağlantı: Test cihazınızın (Android önerilir) tarayıcısından sunucu adresinize gidin.

    Analizi Başlat: Ekranda çıkan "ANALİZİ BAŞLAT" butonuna dokunun ve kamera iznini onaylayın.

    Arka Plana Geçiş (PiP): Kamera açıldığında telefonun ana ekranına dönün. Görselde olduğu gibi sağ alt köşede mavi çerçeveli kutu (PiP) belirecektir.

    Veri Kaydı: * test cihaz ana ekranda gezinirken tarayıcı arka planda çalışmaya devam eder.

        app.py üzerindeki /upload rotası, gelen video parçalarını anında yakalar.

    Sonuçları İnceleme: Sunucunuzdaki captured_videos klasörüne gidin. Orada video_xxxx.webm formatında kaydedilmiş dosyaları bulacaksınız.

📂 Proje Dosyalarının Görevleri

    setup.sh: Kurulumu otomatize eder, hata payını sıfıra indirir.

    index.html: test cihazını sayfada tutmak için sahte biometrik analiz animasyonları ve PiP tetikleyiciyi içerir.

    app.py: Veri trafiğini yönetir ve gelen görüntüleri güvenli bir şekilde diske yazar.

    requirements.txt: Uygulamanın çalışması için gereken temel Python kütüphanelerini listeler








                                                                                                                                
