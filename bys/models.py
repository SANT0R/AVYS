import time
from datetime import date, datetime

from django.contrib.auth.models import User
from django.db import models

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
    tarih = models.CharField(max_length=10,db_column='Tarih',verbose_name="Tarih",default=date.today,blank=False, null=True)
    tür = models.CharField(max_length=20,db_column='TÜR',verbose_name="Tür",default="ISI Makale",blank=False, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",default="Ek dosya",blank=False, null=True)
    

    def get_year(self):
        trh=datetime.strptime(str(self.tarih),'%Y-%m-%d') 
        year=int(datetime.strftime(trh,'%Y'))
        return year



class proje(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.CharField(max_length=10,db_column='Tarih',verbose_name="Tarih",default=date.today,blank=False, null=True)
    tür = models.CharField(max_length=20,db_column='TÜR',verbose_name="Tür",default="TÜBİTAK Projesi",blank=False, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",default="Ek dosya",blank=False, null=True)
     
 
    def get_year(self):
        trh=datetime.strptime(str(self.tarih),'%Y-%m-%d') 
        year=int(datetime.strftime(trh,'%Y'))
        return year



class faliyet(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.CharField(max_length=10,db_column='Tarih',verbose_name="Tarih",default=date.today,blank=False, null=True)
    tür = models.CharField(max_length=20,db_column='TÜR',verbose_name="Tür",default="Baş Editör",blank=False, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",default="Ek dosya",blank=False, null=True)
     
 

    def get_year(self):
        trh=datetime.strptime(str(self.tarih),'%Y-%m-%d') 
        year=int(datetime.strftime(trh,'%Y'))
        return year



class etkinlik(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.CharField(max_length=10,db_column='Tarih',verbose_name="Tarih",default=date.today,blank=False, null=True)
    tür = models.CharField(max_length=20,db_column='TÜR',verbose_name="Tür",default="Kongre Sempozyumu",blank=False, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",default="Ek dosya",blank=False, null=True)
    
 

    def get_year(self):
        trh=datetime.strptime(str(self.tarih),'%Y-%m-%d') 
        year=int(datetime.strftime(trh,'%Y'))
        return year


class atıf(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.CharField(max_length=10,db_column='Tarih',verbose_name="Tarih",default=date.today,blank=False, null=True)
    tür = models.CharField(max_length=20,db_column='TÜR',verbose_name="Tür",default="ISI Dergilerindeki Atıflar",blank=False, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",default="Ek dosya",blank=False, null=True)
       
    

    def get_year(self):
        trh=datetime.strptime(str(self.tarih),'%Y-%m-%d') 
        year=int(datetime.strftime(trh,'%Y'))
        return year



class patent(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.CharField(max_length=10,db_column='Tarih',verbose_name="Tarih",default=date.today,blank=False, null=True)
    tür = models.CharField(max_length=20,db_column='TÜR',verbose_name="Tür",default="Patent", blank=False, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",default="Ek dosya",blank=False, null=True)
        
    
 
    def get_year(self):
        trh=datetime.strptime(str(self.tarih),'%Y-%m-%d') 
        year=int(datetime.strftime(trh,'%Y'))
        return year



class ödül(models.Model):
    akademisyen = models.ForeignKey(User,on_delete=models.CASCADE)
    tarih = models.CharField(max_length=10,db_column='Tarih',verbose_name="Tarih",default=date.today,blank=False, null=True)
    tür = models.CharField(max_length=20,db_column='TÜR',verbose_name="Tür",default="Proje ödülü",blank=False, null=True)
    dosya= models.FileField(upload_to='uploads/',verbose_name="dosyalar",default="Ek dosya",blank=False, null=True)
       
    
 
    def get_year(self):
        trh=datetime.strptime(str(self.tarih),'%Y-%m-%d') 
        year=int(datetime.strftime(trh,'%Y'))
        return year
