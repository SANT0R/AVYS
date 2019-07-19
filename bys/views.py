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
    

        ısımakales=[]
        digermakales=[]
        kitaps=[]
        kitaptabolums=[]
        bildiris=[]
        ansiklopedis=[]
        digers=[]
        yıls=[]
        toplams=[]

    
        ısımakale=yayınlar.filter(tür='ISI Makale')
        digermakale=yayınlar.filter(tür='Diğer Makale')
        kitap=yayınlar.filter(tür='Kitap')
        kitaptabolum=yayınlar.filter(tür='Kitapta Bölüm')
        bildiri=yayınlar.filter(tür='Bildiri')
        ansiklopedi=yayınlar.filter(tür='Ansiklopedi Konusu')
        diger=yayınlar.filter(tür='Diğer')



        tısı=0
        tdgrm=0
        tktp=0
        tktpblm=0
        tbldr=0
        tanskpd=0
        tdgr=0
        yil=2015
        while(True):
            sum=0
            toplam=0
            for ısı in ısımakale:
                
                if ısı.get_year()==yil:
                    sum+=1
                    tısı+=1
                
            toplam+=sum
            ısımakales.append(sum)
            sum=0

            for dgrm in digermakale:
                if dgrm.get_year()==yil:
                    sum+=1
                    tdgrm+=1

            toplam+=sum
            digermakales.append(sum)
            sum=0

            for ktp in kitap:
                if ktp.get_year()==yil:
                    sum+=1
                    tktp+=1


            toplam+=sum
            kitaps.append(sum)
            sum=0

            for ktpblm in kitaptabolum:
                if ktpblm.get_year()==yil:
                    sum+=1
                    tktpblm+=1


            toplam+=sum
            kitaptabolums.append(sum)
            sum=0
            for bldr in bildiri:
                if bldr.get_year()==yil:
                    sum+=1


            toplam+=sum
            bildiris.append(sum)
            sum=0

            for ansk in ansiklopedi:
                if ansk.get_year()==yil:
                    sum+=1
                    tanskpd+=1


            toplam+=sum
            ansiklopedis.append(sum)
            sum=0

            for dgr in diger:
                if dgr.get_year()==yil:
                    sum+=1
                    tdgr+=1
            
            
            toplam+=sum
            digers.append(sum)

            toplams.append(toplam)
            yıls.append(yil)
            yil+=1
            if yil > date.year:
                break
            
        yıls.append("Toplam")
        ısımakales.append(tısı)
        digermakales.append(tdgrm)
        kitaps.append(tktp)
        kitaptabolums.append(tktpblm)
        bildiris.append(tbldr)
        ansiklopedis.append(tanskpd)
        digers.append(tdgr)

        context = {
            "yayınlar":yayınlar,
            "yıls":yıls,
            "ısımakales":ısımakales,
            "digermakales":digermakales,
            "kitaps":kitaps,
            "kitaptabolums":kitaptabolums,
            "bildiris":bildiris,
            "ansiklopedis":ansiklopedis,
            "digers":digers,
            "toplams":toplams,
        }

        return render(request,'yayın rapor.html',context)



def projerapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        projeler=proje.objects.all()
        date=datetime.now()
    

        tubitaks=[]
        sanayis=[]
        kalkınmas=[]
        baps=[]
        digerulusals=[]
        abcs=[]
        abds=[]
        uluslararasıs=[]
        digers=[]
        yıls=[]
        toplams=[]

    
        tubitak=projeler.filter(tür='TÜBİTAK Projesi')
        sanayi=projeler.filter(tür='Sanayi Tezleri Araştırma Projesi')
        kalkınma=projeler.filter(tür='Kalkınma Bakanlığı Destekli Proje')
        bap=projeler.filter(tür='BAP Destekli Araştırma Projesi')
        digerulusal=projeler.filter(tür='Diğer Ulusal Kurumlarca Desteklenen Projeler')
        abc=projeler.filter(tür='Avrupa Birliği Çerçeve Projesi')
        abd=projeler.filter(tür='Avrupa Birliği Destekli Diğer Projeler')
        uluslararası=projeler.filter(tür='Uluslararası Kurumlarca Bilimsel Arştırma Projesi')
        diger=projeler.filter(tür='Diğer')



        ttubi=0
        tsny=0
        tklknm=0
        tbp=0
        tdgrulsl=0
        tac=0
        tad=0
        tulsrr=0
        tdgr=0
        yil=2015
        while(True):
            sum=0
            toplam=0
            for tubi in tubitak:
                
                if tubi.get_year()==yil:
                    sum+=1
                    ttubi+=1
                
            toplam+=sum
            tubitaks.append(sum)
            sum=0

            for sny in sanayi:
                if sny.get_year()==yil:
                    sum+=1
                    tsny+=1

            toplam+=sum
            sanayis.append(sum)
            sum=0

            for klknm in kalkınma:
                if klknm.get_year()==yil:
                    sum+=1
                    tklknm+=1


            toplam+=sum
            kalkınmas.append(sum)
            sum=0

            for bp in bap:
                if bp.get_year()==yil:
                    sum+=1
                    tbp+=1


            toplam+=sum
            baps.append(sum)
            sum=0

            for dgrulsl in digerulusal:
                if dgrulsl.get_year()==yil:
                    sum+=1
                    tdgrulsl+=1


            toplam+=sum
            digerulusals.append(sum)
            sum=0

            for ac in abc:
                if ac.get_year()==yil:
                    sum+=1
                    tac+=1


            toplam+=sum
            abcs.append(sum)
            sum=0

            for ad in abd:
                if ad.get_year()==yil:
                    sum+=1
                    tad+=1


            toplam+=sum
            abds.append(sum)
            sum=0

            for ulsrr in uluslararası:
                if ulsrr.get_year()==yil:
                    sum+=1
                    tulsrr+=1


            toplam+=sum
            uluslararasıs.append(sum)
            sum=0

            for dgr in diger:
                if dgr.get_year()==yil:
                    sum+=1
                    tdgr+=1
            
            
            toplam+=sum
            digers.append(sum)


            toplams.append(toplam)
            yıls.append(yil)
            yil+=1
            if yil > date.year:
                break
            

        yıls.append("Toplam")
        tubitaks.append(ttubi)
        sanayis.append(tsny)
        kalkınmas.append(tklknm)
        baps.append(tbp)
        digerulusals.append(tdgrulsl)
        abcs.append(tac)
        abds.append(tad)
        uluslararasıs.append(tulsrr)
        digers.append(tdgr)

        context = {
            "projeler":projeler,
            "yıls":yıls,
            "tubitaks":tubitaks,
            "sanayis":sanayis,
            "kalkınmas":kalkınmas,
            "baps":baps,
            "digerulusals":digerulusals,
            "abcs":abcs,
            "abds":abds,
            "uluslararasıs":uluslararasıs,
            "digers":digers,
            "toplams":toplams,
        }

        return render(request,'proje rapor.html',context)



def faliyetrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        faliyetler=faliyet.objects.all()
        date=datetime.now()
    

        baseditors=[]
        editors=[]
        yrdeditors=[]
        ozelseditors=[]
        yayınkuyesis=[]
        degerlendirmekuyesis=[]
        danısmakuyesis=[]
        toplams=[]
    
        baseditor=faliyetler.filter(tür='Baş Editör')
        editor=faliyetler.filter(tür='Editör')
        yrdeditor=faliyetler.filter(tür='Yrd.Editör')
        ozelseditor=faliyetler.filter(tür='Özel S.Editörü')
        yayınkuyesi=faliyetler.filter(tür='Yayın K.Üyesi')
        degerlendirmekuyesi=faliyetler.filter(tür='Değerlendirme K.üyesi')
        danısmakuyesi=faliyetler.filter(tür='Danışma K.Üyesi')



        tbsedtr=0
        tedtr=0
        tyedtr=0
        toedtr=0
        tyynu=0
        tdgru=0
        tdnsu=0
        
        yıls=[]
        yil=2015
        while(True):
            sum=0
            toplam=0
            for bsedtr in baseditor:
                
                if bsedtr.get_year()==yil:
                    sum+=1
                    tbsedtr+=1
                
            toplam+=sum
            baseditors.append(sum)
            sum=0

            for edtr in editor:
                if edtr.get_year()==yil:
                    sum+=1
                    tedtr+=1

            toplam+=sum
            editors.append(sum)
            sum=0

            for yedtr in yrdeditor:
                if yedtr.get_year()==yil:
                    sum+=1
                    tyedtr+=1


            toplam+=sum
            yrdeditors.append(sum)
            sum=0

            for oedtr in ozelseditor:
                if oedtr.get_year()==yil:
                    sum+=1
                    toedtr+=1


            toplam+=sum
            ozelseditors.append(sum)
            sum=0

            for yynu in yayınkuyesi:
                if yynu.get_year()==yil:
                    sum+=1
                    tyynu+=1


            toplam+=sum
            yayınkuyesis.append(sum)
            sum=0

            for dgru in degerlendirmekuyesi:
                if dgru.get_year()==yil:
                    sum+=1
                    tdgru+=1


            toplam+=sum
            degerlendirmekuyesis.append(sum)
            sum=0

            for dnsu in danısmakuyesi:
                if dnsu.get_year()==yil:
                    sum+=1
                    tdnsu+=1


            toplam+=sum
            danısmakuyesis.append(sum)


            toplams.append(toplam)
            yıls.append(yil)
            yil+=1
            if yil > date.year:
                break
            
        yıls.append("Toplam")
        baseditors.append(tbsedtr)
        editors.append(tedtr)
        yrdeditors.append(tyedtr)
        ozelseditors.append(toedtr)
        yayınkuyesis.append(tyynu)
        degerlendirmekuyesis.append(tdgru)
        danısmakuyesis.append(tdnsu)

        context = {
            "faliyetler":faliyetler,
            "yıls":yıls,
            "baseditors":baseditors,
            "editors":editors,
            "yrdeditors":yrdeditors,
            "ozelseditors":ozelseditors,
            "yayınkuyesis":yayınkuyesis,
            "degerlendirmekuyesis":degerlendirmekuyesis,
            "danısmakuyesis":danısmakuyesis,
            "toplams":toplams,
        }

        return render(request,'faliyet rapor.html',context)



def etkinlikrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        etkinlikler=etkinlik.objects.all()
        date=datetime.now()
    

        kongres=[]
        calıstays=[]
        sanatsals=[]
        sosyals=[]
        sportifs=[]
        toplams=[]
    
        kongre=etkinlikler.filter(tür='Kongre Sempozyumu')
        calıstay=etkinlikler.filter(tür='Çalıştay')
        sanatsal=etkinlikler.filter(tür='Sanatsal Faliyet')
        sosyal=etkinlikler.filter(tür='Sosyal Faliyet')
        sportif=etkinlikler.filter(tür='Sportif Faliyet')



        tkngr=0
        tclsty=0
        tsnt=0
        tssyl=0
        tsprtf=0
        
        yıls=[]
        yil=2015
        while(True):
            sum=0
            toplam=0
            for kngr in kongre:
                
                if kngr.get_year()==yil:
                    sum+=1
                    tkngr+=1
                
            toplam+=sum
            kongres.append(sum)
            sum=0

            for clsty in calıstay:
                if clsty.get_year()==yil:
                    sum+=1
                    tclsty+=1

            toplam+=sum
            calıstays.append(sum)
            sum=0

            for snt in sanatsal:
                if snt.get_year()==yil:
                    sum+=1
                    tsnt+=1


            toplam+=sum
            sanatsals.append(sum)
            sum=0

            for ssyl in sosyal:
                if ssyl.get_year()==yil:
                    sum+=1
                    tssyl+=1


            toplam+=sum
            sosyals.append(sum)
            sum=0

            for sprtf in sportif:
                if sprtf.get_year()==yil:
                    sum+=1
                    tsprtf+=1


            toplam+=sum
            sportifs.append(sum)
            sum=0



            toplams.append(toplam)
            yıls.append(yil)
            yil+=1
            if yil > date.year:
                break
            
        yıls.append("Toplam")
        kongres.append(tkngr)
        calıstays.append(tclsty)
        sanatsals.append(tsnt)
        sosyals.append(tssyl)
        sportifs.append(tsprtf)

        context = {
            "etkinlikler":etkinlikler,
            "yıls":yıls,
            "kongres":kongres,
            "calıstays":calıstays,
            "sanatsals":sanatsals,
            "sosyals":sosyals,
            "sportifs":sportifs,
            "toplams":toplams,
        }

        return render(request,'etkinlik rapor.html',context)



def atıfrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        atıflar=atıf.objects.all()
        date=datetime.now()
    

        ısıdergis=[]
        dgrulsrrs=[]
        ulusals=[]
        toplams=[]
    
        ısıdergi=atıflar.filter(tür='ISI Dergilerindeki Atıflar')
        dgrulsrr=atıflar.filter(tür='Diğer Uluslar Arası Atıflar')
        ulusal=atıflar.filter(tür='Ulusal Atıflar')



        tısı=0
        tdgruls=0
        tulsl=0
        
        yıls=[]
        yil=2015
        while(True):
            sum=0
            toplam=0
            for ısı in ısıdergi:
                
                if ısı.get_year()==yil:
                    sum+=1
                    tısı+=1
                
            toplam+=sum
            ısıdergis.append(sum)
            sum=0

            for dgruls in dgrulsrr:
                if dgruls.get_year()==yil:
                    sum+=1
                    tdgruls+=1

            toplam+=sum
            dgrulsrrs.append(sum)
            sum=0

            for ulsl in ulusal:
                if ulsl.get_year()==yil:
                    sum+=1
                    tulsl+=1


            toplam+=sum
            ulusals.append(sum)
            sum=0



            toplams.append(toplam)
            yıls.append(yil)
            yil+=1
            if yil > date.year:
                break
            
        yıls.append("Toplam")
        ısıdergis.append(tısı)
        dgrulsrrs.append(tdgruls)
        ulusals.append(tulsl)

        context = {
            "etkinlikler":etkinlikler,
            "yıls":yıls,
            "ısıdergis":ısıdergis,
            "dgrulsrrs":dgrulsrrs,
            "ulusals":ulusals,
            "toplams":toplams,
        }

        return render(request,'atıf rapor.html',context)



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
