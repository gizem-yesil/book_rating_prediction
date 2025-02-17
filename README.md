# **KİTAP PUAN TAHMİNİ API PROJESİ**
Bu proje, kullanıcı yorumlarına dayalı olarak kitapların puanlarını tahmin eden bir makine öğrenmesi modelini ve bu modelin test edildiği bir API'yi içermektedir. API, FastAPI kullanılarak geliştirilmiş ve Docker ile paketlenerek dağıtımı kolay hale getirilmiştir.

# 1.VERİ SETİ :

Veri seti json formatındadır. 9600 kayıttan oluşmaktadır. Eksik değer içermemektedir.Sütunlar:
helpful : yorumun faydalı olması oranı (object)
rating : puan (int64)
reviewText : yorum yazısı (object)
reviewTime : yorum tarihi (object)
summary : yorumun özeti (object)

# 2.VERİ ÖN İŞLEME :

Veri Dönüştürme & Temizlik:

-JSON formatındaki veri, normalize edilerek bir pandas dataframe'ine dönüştürüldü.
-Veri tipleri incelendi, eksik değer olup olmadığı kontrol edildi.
-Puan (rating) dağılımı analiz edildi.

Korelasyon Analizi:

-Sayısal sütunların rating ile ilişkisi incelendi. Anlamlı bir korelasyon bulunamadığı için tamamen metin odaklı bir model geliştirilmesine karar verildi.

Metin Ön İşleme:

-Tüm kelimeler küçük harfe dönüştürüldü.
-Stopword'ler (önemsiz kelimeler) temizlendi.
-Noktalama işaretleri kaldırıldı.
-reviewText ve summary sütunları birleştirilerek "combined_text" sütunu oluşturuldu.

Veri Kaydetme:

-İşlenmiş veri, model eğitiminde kullanılmak üzere pickle formatında kaydedildi.

# 3.MODEL EĞİTİMİ :

**LSTM:**

Derin öğrenmede sıralı veriler ve duygu analizi konularında başarılı olduğu için LSTM (Long Short-Term Memory) modeli tercih edildi.

-Veri seti %20 test , %80 eğitim verisi olarak ayrıldı. Eğitim verilerinin %10'u validasyon için kullanıldı.
-Kelimelerden token'lar oluşturuldu
 -Uygun padding uzunluğu belirlendi.

**Hiperparametre Optimizasyonu:**
 
-Keras tuner kullanıldı.
-Parametreler:
 embedding_dim: 100-300 
 lstm_units: 64-256 
 dropout: 0.2-0.5 

-En iyi validasyon accuracy'si 0.48 olarak bulundu.

**RANDOM FOREST:**

Daha basit bir makine öğrenmesi modeli olarak RF modeli eğitilerek kıyaslama yapıldı.

-Veri seti %20 test , %80 eğitim verisi olarak ayrıldı.
-Padding işlemi uygulandı.
-Word2Vec modeli oluşturularak kelimeler vektörlere dönüştürüldü.

**Hiperparametre Optimizasyonu:**

-GridSearch kullanıldı.
-Parametreler:
n_estimators: 100-500 
max_depth: 10-20 
min_samples_split: (2,5,10) 
min_samples_leaf: (1,2,4) 

-En iyi eğitim accuracy'si 0.75, test accuracy'si 0.34 oldu ,overfitting gözlemlendi

# 4.FAST API ile API GELİŞTİRME :

Projede en iyi performans gösteren modelin API üzerinden kullanılabilir hale getirilmesi için FastAPI kullanıldı.

-/predict endpointinde kullanıcıdan yorumlar alınarak LSTM modeli çalıştırıldı.
-Gönderilen yorumun boş olmaması, belirtilen karakterlerden kısa veya uzun olmaması veya test sırasında yaşanabilecek hatalar gibi kontroller yapıldı. Global exception handler'lar kullanıldı.

Veri Doğrulama & Hata Yönetimi:

-Kullanıcıdan gelen yorumların boş olup olmadığı kontrol edildi.
-Yorumun belirlenen karakter sınırları içinde olup olmadığı denetlendi.
-Beklenmeyen hatalar için global exception handler kullanıldı.

# 5.OPENAPI SPESİFİKASYONU :

-FastApi'nin otomatik oluşturduğu openapi.json verisi manuel düzenleme yapılmak üzere "yaml" formatına dönüştürüldü. 
-Yaml formatı ile API'ye başlık, özet gibi bilgiler eklendi.

# 6.UNIT TESTLER :

-API'nin doğru çalıştığını doğrulamak için pytest kullanılarak testler yazıldı.
-Input formatları, hatalı girişlerde API'nin tepkisi ve model çıktıları test edildi.

# 7.DOCKER KULLANIMI :

-Dockerfile ile proje için bir Docker image oluşturuldu.
-API ve model, bir Docker container'ı içinde çalıştırıldı.


