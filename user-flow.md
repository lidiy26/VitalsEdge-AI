# 🗺️ Kullanıcı Akışı (User Flow) - VitalsEdge AI

## 1. Giriş ve Karşılama
* **Adım:** Kullanıcı uygulamayı açar.
* **Görünüm:** Günlük sağlık skoru (0-100) ve son 24 saatin özeti.

## 2. Veri Kaydı
* **Adım:** Kullanıcı manuel olarak nabız veya semptom (baş ağrısı, yorgunluk) girişi yapar.
* **Görünüm:** Basit form ekranı ve onay simgesi.

## 3. AI Analiz Süreci
* **Adım:** Gemini API arka planda verileri boylamsal (longitudinal) olarak tarar.
* **Görünüm:** "Verileriniz analiz ediliyor..." animasyonu.

## 4. Akıllı Bildirim ve XAI
* **Adım:** Sistem bir anomali tespit ederse kullanıcıyı uyarır.
* **Görünüm:** "Nabız değişkenliğiniz arttı. Nedeni: Düşük uyku kalitesi." (Açıklanabilir YZ).

## 5. Raporlama
* **Adım:** Kullanıcı doktoruna göndermek için rapor oluşturur.
* **Görünüm:** İndirilebilir PDF veya paylaşılabilir özet ekranı.