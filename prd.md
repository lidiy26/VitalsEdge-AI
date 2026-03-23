# 📋 Ürün Gereksinim Dokümanı (PRD): VitalsEdge AI
> **Sürüm:** 1.0.0 | **Kapsam:** Uçtan Uca Sağlık Analitiği

## 1. Ürün Özeti & Vizyon
VitalsEdge AI, reaktif sağlık sistemini (semptom sonrası tedavi) proaktif bir modele (sapma anında önlem) taşır. Kullanıcının biyometrik verilerini boylamsal (zaman serisi) olarak analiz ederek, henüz hissedilmeyen sağlık anomalilerini tespit eder ve XAI (Açıklanabilir YZ) ile gerekçelendirir.

## 2. Kullanıcı Grupları
* **Kullanıcı (Birey):** Sağlık trendlerini izleyen ve risk uyarılarını anlaşılır dilde alan kişi.
* **Hekim (Profesyonel):** Karmaşık veriyi ayıklanmış, trendlere dökülmüş bir "Klinik Özet" olarak inceleyen uzman.

## 3. Temel Özellikler (Key Features)
### 3.1. Boylamsal Analiz & Anomali Tespiti
- **Veri Füzyonu:** Nabız (BPM), uyku kalitesi ve aktivite verilerini birleştirir.
- **Trend Takibi:** Tekil veri yerine "baz çizgisinden sapma" kontrolü yapar (Örn: "Dinlenme nabzın son 30 günün ortalamasının 5 birim üstünde").
### 3.2. Açıklanabilir YZ (XAI) Modülü
- YZ'nin verdiği risk puanının "nedenini" açıklar (Örn: "Düşük derin uyku süresi ve artan solunum hızı korelasyonu nedeniyle bağışıklık uyarısı").
### 3.3. Çok Modlu Veri (Multimodal) İşleme
- Ses analizi (öksürük/nefes) ve metin tabanlı semptom girişlerini klinik veriyle harmanlar.
### 3.4. Dijital İkiz & Simülasyon
- "Eğer bu uyku düzeniyle devam edersen, 15 gün sonraki yorgunluk skorun %40 artacak" gibi projeksiyonlar sunar.

## 4. Teknik Gereksinimler
- **Backend:** Python / Fast API (Zaman serisi analizi için).
- **AI Modelleri:** LSTM (Long Short-Term Memory) veya Transformer modelleri.
- **Güvenlik:** Sağlık verileri için uçtan uca şifreleme ve anonimleştirme.

## 5. Başarı Kriterleri (KPI)
- Atakların (migren, panik atak vb.) en az 12 saat önceden %80 doğrulukla öngörülmesi.
- Kullanıcıların sağlık okuryazarlığında (XAI sayesinde) ölçülebilir artış.