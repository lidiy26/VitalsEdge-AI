# VitalsEdge AI - Görev Listesi

Dayanak: `PRD.md` (Sürüm 1.0.0)

Not: Bu liste, uygulamayı uçtan uca geliştirmek için başlangıç planıdır. Veri türleri, model seçimleri ve UI detayları netleştikçe görevler daha da parçalanabilir.

---

## 1. Kapsam netleştirme ve KPI’lara bağlama
- [ ] PRD’yi MVP / V1 / V2 olarak parçala (migren/panik atak için öncelik)
- [ ] Atak önceden tahmin hedefi için “tanım” üret (label tanımı, olay penceresi)
- [ ] XAI çıktısının ölçülebilir kullanıcı faydasını tanımla (okuryazarlık KPI’sı nasıl ölçülecek)
- [ ] Hekim için “Klinik Özet” şablonunu tasarla (trendler + risk + açıklama)

## 2. Veri modeli ve güvenlik temeli (Privacy by Design)
- [ ] Veri türlerini standardize et: BPM, uyku kalitesi, aktivite, ses (öksürük/nefes), metin semptom girişi
- [ ] Uçtan uca şifreleme ve anahtar yönetimi yaklaşımını belirle
- [ ] Anonimleştirme/pseudonymization stratejisini yaz (hangi alanlar nasıl maskelenir)
- [ ] Veri saklama politikası (retention) ve silme süreçlerini tanımla

## 3. Veri füzyonu (Nabız + uyku + aktivite)
- [ ] Zaman serisi hizalama stratejisi kur (samplerate farklılıkları, eksik veri)
- [ ] Baseline veri temizleme/pipeline’ı kur (outlier, smoothing, missing imputation)
- [ ] “Baz çizgisinden sapma” hesap mantığını prototiple (örn: son 30 gün ortalamasından sapma)
- [ ] Füzyon çıktısını model girişine hazır hale getir (features/dataset)

## 4. Boylamsal analiz & anomali tespiti (Baseline model)
- [ ] Baseline anomali/tahmin modeli seç (LSTM veya Transformer başlangıç planı)
- [ ] Eğitim hedeflerini kur (risk skoru, atak olasılığı, lead-time/penalty)
- [ ] Backtesting ve çapraz doğrulama kurgula
- [ ] Hata analizi için klinik olarak anlamlı metrikleri ekle

## 5. XAI Modülü (Açıklanabilir risk gerekçesi)
- [ ] XAI için açıklama biçimini belirle (özellik katkısı, örüntü bazlı gerekçe, korelasyon temelli anlatım)
- [ ] Modelin ürettiği “risk puan” ile gerekçeyi eşleştiren pipeline’ı yaz
- [ ] Örnek açıklama cümleleri şablonla (kullanıcı dostu dil)
- [ ] Tutarlılık kontrolleri ekle (risk yükselince açıklama da mantıksal olarak değişiyor mu?)

## 6. Çok modlu işleme (Ses + Metin)
- [ ] Ses sinyali için giriş formatını tanımla (sampling rate, event segmentation)
- [ ] Ses model prototipi çıkar (öksürük/nefes sınıflandırma veya embedding)
- [ ] Metin semptom girişlerini normalleştir (etiketleme / semptom dictionary)
- [ ] Multimodal birleştirme stratejisi seç (late fusion / cross-attention vb.)
- [ ] Füzyon çıktısını anomali/risk modeline bağla

## 7. Dijital ikiz & simülasyon (Projections)
- [ ] Projeksiyon hedefini tanımla (örn: 15 gün sonraki yorgunluk skoru)
- [ ] Zaman serisi simülasyon yaklaşımını seç (ileri tahmin + belirsizlik)
- [ ] “Eğer bu uyku düzeniyle devam edersen...” anlatımını üretmek için şema tasarla
- [ ] Belirsizlik/fail-safe yaklaşımı ekle (tahmin güvenilir değilse nasıl davranacak?)

## 8. Ürün arayüzleri (Kullanıcı ve Hekim)
- [ ] Kullanıcı ekranı tasarla: trendler, anomali bayrakları, risk uyarısı + XAI gerekçesi
- [ ] Hekim ekranı tasarla: “Klinik Özet”, ilgili dönem trendleri, açıklama özetleri
- [ ] Bildirim/uyarı akışı kur (lead time 12 saat hedefiyle uyum)
- [ ] Geri bildirim mekanizması ekle (yanlış alarm/kaçırılan atak işaretleme)

## 9. API servisleri ve mimari
- [ ] FastAPI endpoint’lerini tanımla (ingest, analiz, açıklama üretimi, projeksiyon)
- [ ] Model servis katmanını kur (versiyonlama, model registry yaklaşımı)
- [ ] İş akışları için job/queue planı yap (büyük batch analiz vs realtime)
- [ ] Log/metric/tracing standartlarını belirle

## 10. Model değerlendirme ve KPI doğrulama
- [ ] Atakların 12 saat önceden %80 doğruluk hedefi için deney planı oluştur
- [ ] Kullanıcı sağlık okuryazarlığı artışı için ölçüm metodunu belirle
- [ ] Klinik anlamlılık değerlendirmesi ekle (hekime yönelik doğrulama)
- [ ] Sistem genel performans hedefleri (latency, batch time) koy

## 11. MVP çıkışı ve iterasyon
- [ ] MVP kapsamını “en az ama çalışır”a indir (ör. BPM+uyku+aktivite + baseline anomali + temel XAI)
- [ ] Pilot test planı hazırla (kullanıcı kohortu, hekim geri bildirimi)
- [ ] Iterasyon backlog’unu oluştur (yanlış alarm azaltma + multimodal ekleme sırası)

