from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from bys.models import NewUserModel
from bys.models import yayın
from bys.models import proje
from bys.models import faliyet
from bys.models import etkinlik
from bys.models import atıf
from bys.models import patent
from bys.models import ödül
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import * # formlar
from django.contrib.auth.decorators import * #görünüm gizlenme
from django.http import * # Http komutları

# Create your views here.


def anasayfa(request):
    return render(request,'anasayfa.html',locals())





def giris(request):
    #Giriş yapan bidaha giremesin
    oku = request.user.id
    if(oku):
        return HttpResponseRedirect('/AVYS/')
    
    form = AuthenticationForm
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        giris_kontrol = AuthenticationForm(data=request.POST)
        if(giris_kontrol.is_valid()):
            kullanici = authenticate(username=username,password=password)
            login(request,kullanici)
            return HttpResponseRedirect('/AVYS/')
    
    return render(request,'giris.html',locals())


def AVYS(request):
    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('AVYS/')
    return render(request,'AVYS.html',locals())
    



def yayınekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('giris/')
    else:
        
        tarih=request.GET.get("tarih")
        tür=request.GET.get("tür")
        dosya=request.GET.get("dosya")
        newyayın=yayın(akademisyen=request.user,tür=tür,tarih=tarih,dosya=dosya)   
        newyayın.save()
        
        return render(request,'yayın ekle.html')




def projeekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('giris/')
    else:
        
        tarih=request.GET.get("tarih")
        tür=request.GET.get("tür")
        dosya=request.GET.get("dosya")
        newproje=proje(akademisyen=request.user,tür=tür,tarih=tarih,dosya=dosya)   
        newproje.save()
        
        return render(request,'proje ekle.html')





def faliyetekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('giris/')
    else:
        
        tarih=request.GET.get("tarih")
        tür=request.GET.get("tür")
        dosya=request.GET.get("dosya")
        newfaliyet=faliyet(akademisyen=request.user,tür=tür,tarih=tarih,dosya=dosya)   
        newfaliyet.save()
        
        return render(request,'faliyet ekle.html')





def etkinlikekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('giris/')
    else:
        
        tarih=request.GET.get("tarih")
        tür=request.GET.get("tür")
        dosya=request.GET.get("dosya")
        newetkinlik=etkinlik(akademisyen=request.user,tür=tür,tarih=tarih,dosya=dosya)   
        newetkinlik.save()
        
        return render(request,'etkinlik ekle.html')





def atıfekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('giris/')
    else:
        
        tarih=request.GET.get("tarih")
        tür=request.GET.get("tür")
        dosya=request.GET.get("dosya")
        newatıf=atıf(akademisyen=request.user,tür=tür,tarih=tarih,dosya=dosya)   
        newatıf.save()
        
        return render(request,'atıf ekle.html')





def patentekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('giris/')
    else:
        
        tarih=request.GET.get("tarih")
        tür=request.GET.get("tür")
        dosya=request.GET.get("dosya")
        newpatent=patent(akademisyen=request.user,tür=tür,tarih=tarih,dosya=dosya)   
        newpatent.save()
        
        return render(request,'patent ekle.html')





def ödülekle(request):
    
    if request.method=="POST":
        return HttpResponseRedirect('giris/')
    else:
        
        tarih=request.GET.get("tarih")
        tür=request.GET.get("tür")
        dosya=request.GET.get("dosya")
        newödül=ödül(akademisyen=request.user,tür=tür,tarih=tarih,dosya=dosya)   
        newödül.save()
        
        return render(request,'ödül ekle.html')




def yayınrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        yayınlar=yayın.objects.all()
        date=datetime.now()
        yil=2015
        
        ısımakale=[date.year-yil]
        digermakale=[date.year-yil]
        kitap=[date.year-yil]
        kitaptabolum=[date.year-yil]
        bildiri=[date.year-yil]
        ansiklopedi=[date.year-yil]
        diger=[date.year-yil]
        toplam=[date.year-yil]

        index=0
        while (yil <= date.year):
            ısımakale.append(len(yayınlar.filter(tür='ISI Makale')))
            digermakale.append(len(yayınlar.filter(tür='Diğer Makale')))
            kitap.append(len(yayınlar.filter(tür='Kitap')))
            kitaptabolum.append(len(yayınlar.filter(tür='Kitapta Bölüm')))
            bildiri.append(len(yayınlar.filter(tür='Bildiri')))
            ansiklopedi.append(len(yayınlar.filter(tür='Ansiklopedi Konusu')))
            diger.append(len(yayınlar.filter(tür='Diğer')))
            toplam.append(len(yayınlar.filter()))
            index+=1
            yil+=1

        context = {
            "yayınlar":yayınlar,
            "yil":yil,
            "date":date,
            "index":index,
            "ısımakale":ısımakale,
            "digermakale":digermakale,
            "kitap":kitap,
            "kitaptabolum":kitaptabolum,
            "bildiri":bildiri,
            "ansiklopedi":ansiklopedi,
            "diger":diger,
            "toplam":toplam,
            
        }

        return render(request,'yayın rapor.html',context)



def projerapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        projeler = proje.objects.all()
        return render(request,'proje rapor.html',{"projeler":projeler})



def faliyetrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        faliyetler = faliyet.objects.all()
        return render(request,'faliyet rapor.html',{"faliyetler":faliyetler})



def etkinlikrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        etkinlikler = etkinlik.objects.all()
        return render(request,'etkinlik rapor.html',{"etkinlikler":etkinlikler})



def atıfrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        atıflar = yayın.objects.all()
        return render(request,'atıf rapor.html',{"atıflar":atıflar})



def patentrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        patentler = patent.objects.all()
        return render(request,'patent rapor.html',{"patentler":patentler})



def ödülrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        ödüller = ödül.objects.all()
        return render(request,'ödül rapor.html',{"ödüller":ödüller})





def cikis_yap(request):
    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('/')
    logout(request)
    return HttpResponseRedirect('/')
