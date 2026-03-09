import sys

def sığınak_kontrol_sistemi():
    """
    Zombi istilası sırasında sığınağa giriş iznini kontrol eden ana fonksiyon.
    Mantıksal operatörler ve hata yönetimi içerir.
    """
    print("\n" + "="*45)
    print("      🧟 ZOMBİ İSTİLASI SIĞINAK SİSTEMİ 🧟")
    print("="*45)
    
    try:
        # 1. VERİLERİ ALALIM (Kullanıcı Dostu Giriş)
        # .strip() ile boşlukları, .lower() ile büyük harf sorunlarını eliyoruz.
        hiz = int(input("\n🏃 Koşu hızınızı giriniz (10-100): "))
        mermi = int(input("🔫 Kalan mermi sayınızı giriniz: "))
        cevap = input("☣️  Isırıldınız mı? (evet/hayır): ").strip().lower()
        
        # Mantıksal Değişken (Boolean)
        isirildi_mi = (cevap == "evet")

        # 2. ALGORİTMA (Mantık Kapıları)
        # Kural: Isırılmamış olmalı VE (Hızı 50'den yüksek OYSA Mermisi 10'dan fazla olmalı)
        onay_durumu = (not isirildi_mi) and (hiz > 50 or mermi > 10)

        # 3. SONUÇ EKRANI (f-string ile)
        print("\n" + "-"*20 + " SONUÇ " + "-"*20)
        
        if onay_durumu:
            print(f"✅ DURUM: GİRİŞ ONAYLANDI!")
            print(f"Hoş geldin! Mevcut hızın ({hiz}) ve mermin ({mermi}) yeterli görüldü.")
        else:
            # Neden reddedildiğini açıklayan kısa mantık (Ternary Operator)
            sebep = "Enfeksiyon tespit edildi!" if isirildi_mi else "Hız veya mermi yetersiz!"
            print(f"❌ DURUM: GİRİŞ REDDEDİLDİ!")
            print(f"Sığınağa alınamazsınız. Sebep: {sebep}")
            
        print("-"*47)

    except ValueError:
        # Kullanıcı sayı yerine metin girerse burası çalışır
        print("\n⚠️ HATA: Lütfen hız ve mermi alanlarına sadece sayı giriniz!")

# C# 'taki Main metodunun Python karşılığı
if __name__ == "__main__":
    sığınak_kontrol_sistemi()
