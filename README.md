## **KİTAP PUAN TAHMİNİ API PROJESİ**
Bu proje, bir kitap hakkındaki kullanıcı yorumlarına göre kitap puanları tahmini yapan makine öğrenmesi modeli ile bu modelin test edildiği bir API içermektedir. Proje ayrıca Docker kullanılarak paketlenmiştir.

# VERİ SETİ 

Veri seti json formatındadır. 9600 kayıttan oluşmaktadır. Eksik değer içermemektedir.Sütunlar:
helpful : yorumun faydalı olması oranı (object)
rating : puan (int64)
reviewText : yorum yazısı (object)
reviewTime : yorum tarihi (object)
summary : yorumun özeti (object)

# VERİ ÖN İŞLEME

Öncelikle json formatındaki veri normalize edilerek bir dataframe haline getirildi. Veri tipleri, boş değer olup olmadığı ve rating dağılımları incelendi. Daha sonra nümerik değerlerin rating'e katkısını incelemek için korelasyon analizi yapıldı. Anlamlı değerlere ulaşılamayınca tamamen metin odaklı bir tahmin modeli kullanılmasına karar verildi.

- Kelimelere küçük harf dönüştürme, stopword'leri silme, noktalama işaretlerini silme gibi uygulamalar yapıldı.
-reviewText ile summary sütunları birleştirilerek "combined_text" sütunu elde edildi.
-Verinin son hali makine öğrenmesi modelinde kullanılmak üzere "pickle" formatında kaydedildi.

# MODEL EĞİTİMİ

**LSTM:**

Sıralı kelime ve duygu analizini iyi yapan yapısından dolayı kitap incelemesi konusunda iyi bir model olabileceği düşünüldü.

-Veri seti %20 test , %80 eğitim verisi olarak ayrıldı. Eğitim verilerinin %10'u validasyon için kullanıldı.
-Daha sonra ilgili sütundan token'lara oluşturuldu.
-Padding işlemi için uygun uzunluğun belirlenmesi için yorum uzunluklarına bakıldı.

**Hiperparametre Optimizasyonu:**
 
-Keras tuner kullanıldı.
-Model oluşturulurken; embedding_dim parametresi için 100-300 aralığı, lstm_units için 64-256 aralığı, dropout için 0.2-0.5 aralığı belirlendi.
-En iyisi validasyon accuracy'si 0.48 olarak bulundu.
-Veri setinin küçüklüğü düşünülerek daha basit bir ml modeli kullanılmaya karar verildi.

**RANDOM FOREST:**

**Hiperparametre Optimizasyonu:**

# FAST API

En iyi olarak belirlenen ml modeli kullanılmak üzere bir FastApi başlatıldı.

-predict endpointinde kullanıcıdan yorumlar alınarak ml modeli çalıştırıldı.
-Gönderilen yorumun boş olmaması, belirtilen karakterlerden kısa veya uzun olmaması veya test sırasında yaşanabilecek hatalar gibi kontroller yapıldı. Global exception handler'lar kullanıldı.

# OPENAPI SPESİFİKASYONU

-FastApi'nin otomatik oluşturduğu openapi.json verisi manuel düzenleme yapılmak üzere "yaml" formatına dönüştürüldü. 
-Yaml formatı ile API'ye başlık, özet gibi bilgiler eklendi.

# UNIT TESTLER

- API'nin doğru çalışıp çalışmadığı, input formatı kontrolü gibi testler yapıldı.

# DOCKER KULLANIMI

-Dockerfile ile bir Docker image'i , bundan da bir container oluşturuldu ve proje bununla çalıştırıldı.

