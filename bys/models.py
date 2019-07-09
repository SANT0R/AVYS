from django.db import models
from django.contrib.auth.models import User

# Create your models here.



Birimler = (
    ('Eğitim Fakültesi', 'Eğitim Fakültesi'),
    ('Fen Edebiyat Fakültesi', 'Fen Edebiyat Fakültesi'),
    ('İktisadi ve İdari Birimler Fakültesi', 'İktisadi ve İdari Birimler Fakültesi'),
    ('İslami İlimler Fakültesi', 'İslami İlimler Fakültesi'),
    ('Eğitim Fakültesi', 'Eğitim Fakültesi'),
    ('Tıp Fakültesi', 'Tıp Fakültesi'),
    ('Patnos Sultan Alparslan Doğa Bilimleri ve Mühendislik Fakültesi', 'Patnos Sultan Alparslan Doğa Bilimleri ve Mühendislik Fakültesi'),
    ('Sağlık Yüksek Okulu', 'Sağlık Yüksek Okulu'),
    ('Beden Eğitimi ve Spor Yüksekokulu', 'Beden Eğitimi ve Spor Yüksekokulu'),
    ('Eleşkirt Celal Oruç Hayvansal Üretim Yüksekokulu', 'Eleşkirt Celal Oruç Hayvansal Üretim Yüksekokulu'),
    ('Yabancı Diller Yüksekokulu', 'Yabancı Diller Yüksekokulu'),
    ('Turizm İşletmeciliği ve Otelcilik Yüksekokulu', 'Turizm İşletmeciliği ve Otelcilik Yüksekokulu'),
    ('Patnos Sosyal Hizmetler Yüksekokulu', 'Patnos Sosyal Hizmetler Yüksekokulu'),
    ('Meslek Yüksekokulu', 'Meslek Yüksekokulu'),
    ('Sağlık Hizmetleri Meslek Yüksekokulu', 'Sağlık Hizmetleri Meslek Yüksekokulu'),
    ('Eleşkirt Meslek Yüksekokulu', 'Eleşkirt Meslek Yüksekokulu'),
    ('Doğubayazıt Ahmed-i Hani Meslek Yüksekokulu', 'Doğubayazıt Ahmed-i Hani Meslek Yüksekokulu'),
    ('Sivil Havacılık Meslek Yüksekokulu', 'Sivil Havacılık Meslek Yüksekokulu'),
    ('Patnos Meslek Yüksekokulu', 'Patnos Meslek Yüksekokulu'),
    ('Fen Bilimleri Enstitüsü', 'Fen Bilimleri Enstitüsü'),
    ('Sosyal Bilimler Enstitüsü', 'Sosyal Bilimler Enstitüsü'),
    ('Sağlık Bilimleri Enstitüsü', 'Sağlık Bilimleri Enstitüsü'),
)

Türler = (
    ('ISI Makale', 'ISI Makale'),
    ('Diğer Makale', 'Diğer Makale'),
    ('Kitap', 'Kitap'),
    ('Kitapta Bölüm', 'Kitapta Bölüm'),
    ('Bildiri', 'Bildiri'),
    ('Ansiklopedi konusu', 'Ansiklopedi konusu'),
    ('Diğer', 'Diğer'),
)

class NewUserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=13,db_column='TEL',verbose_name="Tel",default='+905** *** ** **',blank=True, null=True)
    birim = models.CharField(max_length=150,choices=Birimler,db_column='BİRİM',verbose_name="Birim")

    class Meta:
        verbose_name = "Kullanıcı Ayarları"
 
    def __str__(self):
        return "Kişisel Bilgiler"

class yayın(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.DateField(db_column='Tarih',verbose_name="Tarih", auto_now_add=True,blank=True, null=True)
    tür = models.CharField(max_length=20,choices=Türler,db_column='TÜR',verbose_name="Tür",blank=True, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",blank=True, null=True)


class proje(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.DateField(db_column='Tarih',verbose_name="Tarih", auto_now_add=True,blank=True, null=True)
    tür = models.CharField(max_length=20,choices=Türler,db_column='TÜR',verbose_name="Tür",blank=True, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",blank=True, null=True)

class faliyet(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.DateField(db_column='Tarih',verbose_name="Tarih", auto_now_add=True,blank=True, null=True)
    tür = models.CharField(max_length=20,choices=Türler,db_column='TÜR',verbose_name="Tür",blank=True, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",blank=True, null=True)

class etkinlik(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.DateField(db_column='Tarih',verbose_name="Tarih", auto_now_add=True,blank=True, null=True)
    tür = models.CharField(max_length=20,choices=Türler,db_column='TÜR',verbose_name="Tür",blank=True, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",blank=True, null=True)

class atıf(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.DateField(db_column='Tarih',verbose_name="Tarih", auto_now_add=True,blank=True, null=True)
    tür = models.CharField(max_length=20,choices=Türler,db_column='TÜR',verbose_name="Tür",blank=True, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",blank=True, null=True)

class patent(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.DateField(db_column='Tarih',verbose_name="Tarih", auto_now_add=True,blank=True, null=True)
    tür = models.CharField(max_length=20,choices=Türler,db_column='TÜR',verbose_name="Tür",blank=True, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",blank=True, null=True)

class ödül(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.DateField(db_column='Tarih',verbose_name="Tarih", auto_now_add=True,blank=True, null=True)
    tür = models.CharField(max_length=20,choices=Türler,db_column='TÜR',verbose_name="Tür",blank=True, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",blank=True, null=True)