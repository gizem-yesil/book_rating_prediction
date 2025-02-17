## **KİTAP PUAN TAHMİNİ API PROJESİ**
Bu proje, bir kitap hakkındaki kullanıcı yorumlarına göre kitap puanları tahmini yapan makine öğrenmesi modeli ile bu modelin test edildiği bir API içermektedir. Proje ayrıca Docker kullanılarak paketlenmiştir.

#VERİ SETİ 

Veri seti json formatındadır. 9600 kayıttan oluşmaktadır. Eksik değer içermemektedir.Sütunlar:
helpful : yorumun faydalı olması oranı (object)
rating : puan (int64)
reviewText : yorum yazısı (object)
reviewTime : yorum tarihi (object)
summary : yorumun özeti (object)
