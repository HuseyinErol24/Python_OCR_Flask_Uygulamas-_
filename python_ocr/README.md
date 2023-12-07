# Hüseyin Erol #

# OCR Flask Uygulaması #
- Bu Flask uygulaması, kullanıcının bir görüntü dosyası yükleyebileceği ve ardından bu görüntüdeki metni çıkartabileceği bir basit OCR (Optik Karakter Tanıma) aracını sağlar.

# Kütüphaneler 
- pip install flask pytesseract Pillow
- Tesseract OCR Yükleyin

- Bu uygulama, metni çıkarmak için Tesseract OCR kullanır. Tesseract OCR'nin resmi web sitesinden Tesseract OCR'yı indirip yükleyebilirsiniz. Ardından, pytesseract.pytesseract.tesseract_cmd satırındaki dosya yolunu Tesseract OCR'nin yüklü olduğu konuma güncelleyin.


Varsayılan olarak, uygulama http://127.0.0.1:5000/ adresinde çalışır. Bir web tarayıcısını kullanarak bu adrese giderek uygulamayı ziyaret edebilirsiniz.
# Kullanım

- 1) Görüntü Yükleyin

- 2) Ana sayfada bulunan dosya yükleme formunu kullanarak bir görüntü dosyası yükleyin.

- 3) Sonuçları Görüntüleyin

- 4) Görüntü yüklendikten sonra, uygulama tarafından çıkartılan metni, dosyanın oluşturulma tarihini, erişim tarihini, değişiklik tarihini ve dosya boyutunu göreceksiniz.

Not:
- Bu uygulama, Flask web çerçevesini kullanır. Flask, Python tabanlı hafif bir web çerçevesidir.
- Görüntü üzerinde metin çıkartma işlemi için Tesseract OCR kullanılmıştır.
- Dosya yüklendikten sonra, dosya hemen silinir. Bu, kullanıcının özel bilgilerini korumak için tasarlanmıştır.
