# VitalsEdge AI

## Basla
🩺 VitalsEdge AI - Akıllı Sağlık Analiz Dashboard'u
VitalsEdge, kullanıcıların yaş, nabız ve tansiyon gibi kritik sağlık verilerini takip etmelerini ve bu veriler üzerinden kişiselleştirilmiş risk analizleri almalarını sağlayan modern bir dijital sağlık asistanıdır.

🚀 Problem ve Çözüm
Problem
Bireyler sağlık verilerini (nabız, tansiyon vb.) ölçseler bile, bu verilerin ne anlama geldiğini ve o anki fiziksel durumlarına göre nasıl bir aksiyon almaları gerektiğini anlamakta zorluk çekiyorlar. Ham veriler, uzman bir yorum olmadan kullanıcı için stres kaynağı olabiliyor.

Çözüm (VitalsEdge AI)
VitalsEdge, bu ham verileri alır ve:

Görselleştirir: Kullanıcı dostu bir dashboard üzerinden verileri anlamlı grafiklere dönüştürür.

Yorumlar: Google Gemini 1.5 Flash modelini kullanarak verileri analiz eder ve tıbbi tavsiye yerine geçmeyen, tamamen bilgilendirici ve kişiye özel "Aksiyon Planları" sunar.

Hızlandırır: Localhost veya Cloud üzerinden saniyeler içinde sonuç üreterek zaman kazandırır.


⚙️ Nasıl Çalıştırılır? (Kurulum Rehberi)
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Depoyu Klonlayın
Bash
git clone https://github.com/lidiy26/VitalsEdge-AI.git
cd VitalsEdge
2. Gerekli Kütüphaneleri Kurun
Bash
pip install -r requirements.txt
3. API Anahtarınızı Tanımlayın
main.py dosyası içerisindeki API_KEY değişkenine kendi Google AI Studio anahtarınızı ekleyin.

4. Uygulamayı Başlatın
Bash
python -m streamlit run main.py
📊 Geri Bildirim ve Değerlendirme
Uygulamanın kullanılabilirliğini ve AI çıktı kalitesini ölçmek için 5 kullanıcı ile bir pilot çalışma yürütülmüştür.

Anket Formu: [https://forms.gle/sDetPo7EbZn1xXmYA]

Canlı Demo: [https://project-pal-uploader.lovable.app]

Video Linki:[https://www.loom.com/share/588ea48aa6de45d1873586d508047e3a]
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python main.py
5. http://localhost:8000/api/docs
http://localhost:3000/dashboard.html
http://localhost:3000/dashboard.html
loveable https://github.com/lidiy26/vitalsedge-ai-9c43b057.git
https://project-pal-uploader.lovable.app/
