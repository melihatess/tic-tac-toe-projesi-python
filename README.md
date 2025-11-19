# Python ile Geliştirilen Tic-Tac-Toe Oyunu

> Python kullanılarak geliştirilmiş, Oyuncu ('O') ile Rastgele Bir Şekilde Hamle Yapan Bilgisayar ('X') arasında oynanan basit Tic-Tac-Toe oyun uygulamasıdır.

## Özellikler

* **Tek Oyunculu Mod:** Oyuncu ('O') vs. Bilgisayar ('X').
* **Bilgisayar Başlangış Hamlesi:** Oyun her zaman bilgisayarın tahtanın orta karesini (5 = 'X') almasıyla başlar. 
* **Akıllı Rakip:** Bilgisayar, mevcut boş kareler arasından rastgele bir seçim yaparak hamle yapar.
* **Komut Satırı Arayüzü (CLI):** Kolay ve hızlı başlatma.
* **Kazanan Kontrolü:** Oyun bittiğinde veya berabere kaldığında otomatik olarak sonucu bildirir.

***

## Kurulum ve Başlatma

Bu projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edin.

### Gereksinimler

Projenin çalışması için sadece **Python 3.x** gereklidir.

### Adımlar

1.  **Depoyu Klonlayın:**
    Bu komut ile projeyi bilgisayarınıza indirin:
    ```bash
    git clone https://github.com/melihatess/tic-tac-toe-projesi-python.git
    cd tic-tac-toe-projesi-python
    ```

2.  **Oyunu Başlatın:**
    Projenin ana dosyasını Python yorumlayıcısı ile çalıştırın:
    ```bash
    python main.py
    ```

***

## Kullanım

Oyunu başlattıktan sonra, **siz 'O'** olarak hamle yapacaksınız ve **bilgisayar 'X'** olarak cevap verecektir.

1.  **Oyunu Başlatın:**
    ```bash
    python main.py
    ```
2.  **Oyun Akışı:**
    * Oyun başlar başlamaz bilgisayar ilk hamleyi 5 numarayla yapar.
    * Tahta görüntülendiğinde, boş karelerin **1'den 9'a kadar olan numarasını** girerek hamlenizi yapın.

**Tahta Numaralandırması:** 
Hamle yaparken tahtayı aşağıdaki gibi hayal edin:

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

**Örnek Hamle:**
* Tahta görüntülendikten ve bilgisayar hamlesini yaptıktan sonra, sol alt köşeye oynamak için **7** girin:
    ```
    Hamleni yap (1-9): 7
    ```
* Ardından bilgisayar otomatik olarak sıradaki hamlesini yapacaktır.
  
***

## Katkıda Bulunma

Projenin geliştirilmesine katkıda bulunmak isterseniz çok memnun olurum.

* 1.  Depoyu (Fork) çatallayın.
* 2.  Yeni bir özellik veya hata düzeltmesi için bir dal (branch) oluşturun. (`git checkout -b feature/YeniOzellik`)
* 3.  Değişikliklerinizi kaydedin. (`git commit -m 'Yeni özellik: Aciklama'`)
* 4.  Dalı yükleyin. (`git push origin feature/YeniOzellik`)
* 5.  Bir **Pull Request** açın.

***

## Lisans

Bu proje **MIT Lisansı** altında yayımlanmıştır. Bu, herkesin projeyi kullanabileceği, değiştirebileceği ve dağıtabileceği anlamına gelir. Lisansın tam metni için lütfen [LICENSE](LICENSE) dosyasına bakın.  Şimdi nasıl?

***

## İletişim
Meliha Ateş - melihates9407@gmail.com
