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

        tarih=request.POST.get("tarih")
        tür=request.POST.get("tür")
        dosya=request.POST.get("dosya")
        akademisyen=NewUserModel.objects.filter(user=request.user)

        newyayın=yayın(akademisyen=akademisyen[0],tür=tür,tarih=tarih,dosya=dosya)
        newyayın.save()
    
   
    return render(request,'yayın ekle.html')




def projeekle(request):
    
    if request.method=="POST":

        tarih=request.POST.get("tarih")
        tür=request.POST.get("tür")
        dosya=request.POST.get("dosya")
        akademisyen=NewUserModel.objects.filter(user=request.user)

        newproje=proje(akademisyen=akademisyen[0],tür=tür,tarih=tarih,dosya=dosya)   
        newproje.save()
        
    return render(request,'proje ekle.html')





def faliyetekle(request):
    
    if request.method=="POST":

        tarih=request.POST.get("tarih")
        tür=request.POST.get("tür")
        dosya=request.POST.get("dosya")
        akademisyen=NewUserModel.objects.filter(user=request.user)

        newfaliyet=faliyet(akademisyen=akademisyen[0],tür=tür,tarih=tarih,dosya=dosya)   
        newfaliyet.save()
        
    return render(request,'faliyet ekle.html')





def etkinlikekle(request):
    
    if request.method=="POST":

        tarih=request.POST.get("tarih")
        tür=request.POST.get("tür")
        dosya=request.POST.get("dosya")
        akademisyen=NewUserModel.objects.filter(user=request.user)

        newetkinlik=etkinlik(akademisyen=akademisyen[0],tür=tür,tarih=tarih,dosya=dosya)   
        newetkinlik.save()
        
    return render(request,'etkinlik ekle.html')





def atıfekle(request):
    
    if request.method=="POST":

        tarih=request.POST.get("tarih")
        tür=request.POST.get("tür")
        dosya=request.POST.get("dosya")
        akademisyen=NewUserModel.objects.filter(user=request.user)

        newatıf=atıf(akademisyen=akademisyen[0],tür=tür,tarih=tarih,dosya=dosya)   
        newatıf.save()
        
    return render(request,'atıf ekle.html')





def patentekle(request):
    
    if request.method=="POST":

        tarih=request.POST.get("tarih")
        tür=request.POST.get("tür")
        dosya=request.POST.get("dosya")
        akademisyen=NewUserModel.objects.filter(user=request.user)

        newpatent=patent(akademisyen=akademisyen[0],tür=tür,tarih=tarih,dosya=dosya)   
        newpatent.save()
        
    return render(request,'patent ekle.html')





def ödülekle(request):
    
    if request.method=="POST":

        tarih=request.POST.get("tarih")
        tür=request.POST.get("tür")
        dosya=request.POST.get("dosya")
        akademisyen=NewUserModel.objects.filter(user=request.user)

        newödül=ödül(akademisyen=akademisyen[0],tür=tür,tarih=tarih,dosya=dosya)   
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

    
        ısımakale=yayınlar.filter(tür='ISI Dergilerinde Makale')
        digermakale=yayınlar.filter(tür='Diğer Dergilerde Makale')
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
            "atıflar":atıflar,
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
        
        patentler=patent.objects.all()
        date=datetime.now()
    

        patents=[]
        fydlmdls=[]
        toplams=[]
    
        patnt=patentler.filter(tür='Patent')
        fydlmdl=patentler.filter(tür='Faydalı Model')



        tptnt=0
        tfydmdl=0
        
        yıls=[]
        yil=2015
        while(True):
            sum=0
            toplam=0
            for ptnt in patnt:
                
                if ptnt.get_year()==yil:
                    sum+=1
                    tptnt+=1
                
            toplam+=sum
            patents.append(sum)
            sum=0

            for fydmdl in fydlmdl:
                if fydmdl.get_year()==yil:
                    sum+=1
                    tfydmdl+=1

            toplam+=sum
            fydlmdls.append(sum)
            sum=0

            toplams.append(toplam)
            yıls.append(yil)
            yil+=1
            if yil > date.year:
                break
            
        yıls.append("Toplam")
        patents.append(tptnt)
        fydlmdls.append(tfydmdl)

        context = {
            "patentler":patentler,
            "yıls":yıls,
            "patents":patents,
            "fydlmdls":fydlmdls,
            "toplams":toplams,
        }

        return render(request,'patent rapor.html',context)




def ödülrapor(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        ödüller=ödül.objects.all()
        date=datetime.now()
    

        projes=[]
        bilims=[]
        burss=[]
        digers=[]
        toplams=[]
    
        proje=ödüller.filter(tür='Proje Ödülü')
        bilim=ödüller.filter(tür='Bil. çalışma ödülü')
        burs=ödüller.filter(tür='Burslar')
        diger=ödüller.filter(tür='Diğer ödüller')



        tprj=0
        tblm=0
        tbrs=0
        tdgr=0
        
        yıls=[]
        yil=2015
        while(True):
            sum=0
            toplam=0
            for prj in proje:
                if prj.get_year()==yil:
                    sum+=1
                    tprj+=1
                
            toplam+=sum
            projes.append(sum)
            sum=0

            for blm in bilim:
                if blm.get_year()==yil:
                    sum+=1
                    tblm+=1

            toplam+=sum
            bilims.append(sum)
            sum=0

            sum=0
            toplam=0
            for brs in burs:
                if brs.get_year()==yil:
                    sum+=1
                    tbrs+=1
                
            toplam+=sum
            burss.append(sum)
            sum=0

            for dgr in diger:
                if dgr.get_year()==yil:
                    sum+=1
                    tdgr+=1

            toplam+=sum
            digers.append(sum)
            sum=0



            toplams.append(toplam)
            yıls.append(yil)
            yil+=1
            if yil > date.year:
                break
            
        yıls.append("Toplam")
        projes.append(tprj)
        bilims.append(tblm)
        burss.append(tbrs)
        digers.append(tdgr)

        context = {
            "ödüller":ödüller,
            "yıls":yıls,
            "projes":projes,
            "bilims":bilims,
            "burss":burss,
            "digers":digers,
            "toplams":toplams,
        }

        return render(request,'ödül rapor.html',context)

















birims=[]
birims.append('Eğitim Fakültesi')
birims.append('Fen Edebiyat Fakültesi')
birims.append('İktisadi ve İdari Birimler Fakültesi')
birims.append('İslami İlimler Fakültesi')
birims.append('Tıp Fakültesi')
birims.append('Patnos Sultan Alparslan Doğa Bilimleri ve Mühendislik Fakültesi')
birims.append('Sağlık Yüksek Okulu')
birims.append('Beden Eğitimi ve Spor Yüksekokulu')
birims.append('Eleşkirt Celal Oruç Hayvansal Üretim Yüksekokulu')
birims.append('Yabancı Diller Yüksekokulu')
birims.append('Turizm İşletmeciliği ve Otelcilik Yüksekokulu')
birims.append('Patnos Sosyal Hizmetler Yüksekokulu')
birims.append('Meslek Yüksekokulu')
birims.append('Sağlık Hizmetleri Meslek Yüksekokulu')
birims.append('Eleşkirt Meslek Yüksekokulu')
birims.append('Doğubayazıt Ahmed-i Hani Meslek Yüksekokulu')
birims.append('Sivil Havacılık Meslek Yüksekokulu')
birims.append('Patnos Meslek Yüksekokulu')
birims.append('Fen Bilimleri Enstitüsü')
birims.append('Sosyal Bilimler Enstitüsü')
birims.append('Sağlık Bilimleri Enstitüsü')

def yayınrapor2(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        yayınlar=yayın.objects.all()
        date=datetime.now()


        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]
        yils=[]
        tyil=[]
        tyil.append("Toplam")

        context={
            "yayınlar":yayınlar,
            "yils":yils,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
            "tyil":tyil,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1
        tyilindex=0
        yil=2015
        maxyil=date.year-yil

        for birim in birims:
            yil=2015
            yilindex=1
            toplam=0
            while True:
                if maxyil >= tyilindex:
                    tyil.append(0)
                
                sum=0
            
                for yyn in yayınlar:

                    if yyn.get_year()==yil and yyn.akademisyen.birim==birim:
                        sum+=1

                toplam+=sum
                tyil[yilindex]+=sum
                context["birim"+str(index)].append(sum)
                
                yilindex+=1
                if maxyil >= tyilindex:
                    yils.append(yil)
                    tyilindex+=1
                yil+=1
                if yil > date.year:
                    break 
            
            context["birim"+str(index)].append(toplam)
            index+=1


        
        yils.append("Toplam")
        return render(request,'yayın rapor2.html',context)






def projerapor2(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        projeler=proje.objects.all()
        date=datetime.now()


        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]
        yils=[]
        tyil=[]
        tyil.append("Toplam")

        context={
            "projeler":projeler,
            "yils":yils,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
            "tyil":tyil,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1
        tyilindex=0
        yil=2015
        maxyil=date.year-yil

        for birim in birims:
            yil=2015
            yilindex=1
            toplam=0
            while True:
                if maxyil >= tyilindex:
                    tyil.append(0)
                
                sum=0
            
                for prj in projeler:

                    if prj.get_year()==yil and prj.akademisyen.birim==birim:
                        sum+=1

                tyil[yilindex]+=sum
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
                yilindex+=1
                if maxyil >= tyilindex:
                    yils.append(yil)
                    tyilindex+=1
                yil+=1
                if yil > date.year:
                    break 
            
            context["birim"+str(index)].append(toplam)
            index+=1


        
        yils.append("Toplam")
        return render(request,'proje rapor2.html',context)






def faliyetrapor2(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        faliyetler=faliyet.objects.all()
        date=datetime.now()


        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]
        yils=[]
        tyil=[]
        tyil.append("Toplam")

        context={
            "faliyetler":faliyetler,
            "yils":yils,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
            "tyil":tyil,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1
        tyilindex=0
        yil=2015
        maxyil=date.year-yil

        for birim in birims:
            yil=2015
            yilindex=1
            toplam=0
            while True:
                if maxyil >= tyilindex:
                    tyil.append(0)
                
                sum=0
            
                for flyt in faliyetler:

                    if flyt.get_year()==yil and flyt.akademisyen.birim==birim:
                        sum+=1

                tyil[yilindex]+=sum
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
                yilindex+=1
                if maxyil >= tyilindex:
                    yils.append(yil)
                    tyilindex+=1
                yil+=1
                if yil > date.year:
                    break 
            
            context["birim"+str(index)].append(toplam)
            index+=1


        
        yils.append("Toplam")
        return render(request,'faliyet rapor2.html',context)






def etkinlikrapor2(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        etkinlikler=etkinlik.objects.all()
        date=datetime.now()


        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]
        yils=[]
        tyil=[]
        tyil.append("Toplam")

        context={
            "etkinlikler":etkinlikler,
            "yils":yils,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
            "tyil":tyil,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1
        tyilindex=0
        yil=2015
        maxyil=date.year-yil

        for birim in birims:
            yil=2015
            yilindex=1
            toplam=0
            while True:
                if maxyil >= tyilindex:
                    tyil.append(0)
                
                sum=0
            
                for etknlk in etkinlikler:

                    if etknlk.get_year()==yil and etknlk.akademisyen.birim==birim:
                        sum+=1

                tyil[yilindex]+=sum
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
                yilindex+=1
                if maxyil >= tyilindex:
                    yils.append(yil)
                    tyilindex+=1
                yil+=1
                if yil > date.year:
                    break 
            
            context["birim"+str(index)].append(toplam)
            index+=1


        
        yils.append("Toplam")
        return render(request,'etkinlik rapor2.html',context)






def atıfrapor2(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        atıflar=atıf.objects.all()
        date=datetime.now()


        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]
        yils=[]
        tyil=[]
        tyil.append("Toplam")

        context={
            "atıflar":atıflar,
            "yils":yils,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
            "tyil":tyil,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1
        tyilindex=0
        yil=2015
        maxyil=date.year-yil

        for birim in birims:
            yil=2015
            yilindex=1
            toplam=0
            while True:
                if maxyil >= tyilindex:
                    tyil.append(0)
                
                sum=0
            
                for atf in atıflar:

                    if atf.get_year()==yil and atf.akademisyen.birim==birim:
                        sum+=1

                tyil[yilindex]+=sum
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
                yilindex+=1
                if maxyil >= tyilindex:
                    yils.append(yil)
                    tyilindex+=1
                yil+=1
                if yil > date.year:
                    break 
            
            context["birim"+str(index)].append(toplam)
            index+=1


        
        yils.append("Toplam")
        return render(request,'atıf rapor2.html',context)






def patentrapor2(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        patentler=patent.objects.all()
        date=datetime.now()


        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]
        yils=[]
        tyil=[]
        tyil.append("Toplam")

        context={
            "patentler":patentler,
            "yils":yils,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
            "tyil":tyil,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1
        tyilindex=0
        yil=2015
        maxyil=date.year-yil

        for birim in birims:
            yil=2015
            yilindex=1
            toplam=0
            while True:
                if maxyil >= tyilindex:
                    tyil.append(0)
                
                sum=0
            
                for ptnt in patentler:

                    if ptnt.get_year()==yil and ptnt.akademisyen.birim==birim:
                        sum+=1

                tyil[yilindex]+=sum
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
                yilindex+=1
                if maxyil >= tyilindex:
                    yils.append(yil)
                    tyilindex+=1
                yil+=1
                if yil > date.year:
                    break 
            
            context["birim"+str(index)].append(toplam)
            index+=1


        
        yils.append("Toplam")
        return render(request,'patent rapor2.html',context)






def ödülrapor2(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        ödüller=ödül.objects.all()
        date=datetime.now()


        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]
        yils=[]
        tyil=[]
        tyil.append("Toplam")

        context={
            "ödüller":ödüller,
            "yils":yils,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
            "tyil":tyil,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1
        tyilindex=0
        yil=2015
        maxyil=date.year-yil

        for birim in birims:
            yil=2015
            yilindex=1
            toplam=0
            while True:
                if maxyil >= tyilindex:
                    tyil.append(0)
                
                sum=0
            
                for ödl in ödüller:

                    if ödl.get_year()==yil and ödl.akademisyen.birim==birim:
                        sum+=1

                tyil[yilindex]+=sum
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
                yilindex+=1
                if maxyil >= tyilindex:
                    yils.append(yil)
                    tyilindex+=1
                yil+=1
                if yil > date.year:
                    break 
            
            context["birim"+str(index)].append(toplam)
            index+=1


        
        yils.append("Toplam")
        return render(request,'ödül rapor2.html',context)























def yayınrapor3(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        yayınlar=yayın.objects.all()


        turs=[]
        turs.append("ISI Dergilerinde Makale")
        turs.append("Diğer Dergilerde Makale")
        turs.append("Kitap")
        turs.append("Kitapta Bölüm")
        turs.append("Bildiri")
        turs.append("Ansiklopedi Konusu")
        turs.append("Diğer")
        ttur=[]
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)

        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]

        context={
            "yayınlar":yayınlar,
            "turs":turs,
            "ttur":ttur,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1

        for birim in birims:
            turindex=0
            toplam=0
            for tur in turs:
                
                sum=0
            
                for yyn in yayınlar:

                    if yyn.tür==tur and yyn.akademisyen.birim==birim:
                        sum+=1
                
                ttur[turindex]+=sum
                turindex+=1
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
            
            
            context["birim"+str(index)].append(toplam)
            index+=1
        
        turs.append("Toplam")

        
        return render(request,'yayın rapor3.html',context)









def projerapor3(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        projeler=proje.objects.all()


        turs=[]
        turs.append("TÜBİTAK Projesi")
        turs.append("Sanayi Tezleri Araştırma Projesi")
        turs.append("Kalkınma Bakanlığı Destekli Proje")
        turs.append("BAP Destekli Araştırma Projesi")
        turs.append("Diğer Ulusal Kurumlarca Desteklenen Projeler")
        turs.append("Avrupa Birliği Çerçeve Projesi")
        turs.append("Avrupa Birliği Destekli Diğer Projesi")
        turs.append("Uluslararası Kurumlarca Bilimsel Araştırma Projesi")
        turs.append("Diğer")
        ttur=[]
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)

        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]

        context={
            "projeler":projeler,
            "turs":turs,
            "ttur":ttur,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1

        for birim in birims:
            turindex=0
            for tur in turs:
                
                sum=0
                toplam=0
            
                for prj in projeler:

                    if prj.tür==tur and prj.akademisyen.birim==birim:
                        sum+=1
                        ttur[turindex]+=sum

                turindex+=1
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
            
            
            context["birim"+str(index)].append(toplam)
            index+=1
        
        turs.append("Toplam")

        
        return render(request,'proje rapor3.html',context)









def faliyetrapor3(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        faliyetler=faliyet.objects.all()


        turs=[]
        turs.append("Baş Editör")
        turs.append("Editör")
        turs.append("Yrd.Editör")
        turs.append("Özel S.Editörü")
        turs.append("Yayın K.Üyesi")
        turs.append("Değerlendirme K.üyesi")
        turs.append("Danışma K.Üyesi")
        ttur=[]
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)
        ttur.append(0)

        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]

        context={
            "faliyetler":faliyetler,
            "turs":turs,
            "ttur":ttur,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1

        for birim in birims:
            turindex=0
            for tur in turs:
                
                sum=0
                toplam=0
            
                for flyt in faliyetler:

                    if flyt.tür==tur and flyt.akademisyen.birim==birim:
                        sum+=1
                        ttur[turindex]+=sum

                turindex+=1
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
            
            
            context["birim"+str(index)].append(toplam)
            index+=1
        
        turs.append("Toplam")

        
        return render(request,'faliyet rapor3.html',context)









def patentrapor3(request):
    if request.method=='POST':
        return HttpResponseRedirect('/anasayfa.html')
    else:
        
        patentler=patent.objects.all()


        turs=[]
        turs.append("Patent")
        turs.append("Faydalı Model")
        ttur=[]
        ttur.append(0)
        ttur.append(0)

        birim1=[]
        birim2=[]
        birim3=[]
        birim4=[]
        birim5=[]
        birim6=[]
        birim7=[]
        birim8=[]
        birim9=[]
        birim10=[]
        birim11=[]
        birim12=[]
        birim13=[]
        birim14=[]
        birim15=[]
        birim16=[]
        birim17=[]
        birim18=[]
        birim19=[]
        birim20=[]
        birim21=[]

        context={
            "patentler":patentler,
            "turs":turs,
            "ttur":ttur,
            "birim1":birim1,
            "birim2":birim2,
            "birim3":birim3,
            "birim4":birim4,
            "birim5":birim5,
            "birim6":birim6,
            "birim7":birim7,
            "birim8":birim8,
            "birim9":birim9,
            "birim10":birim10,
            "birim11":birim11,
            "birim12":birim12,
            "birim13":birim13,
            "birim14":birim14,
            "birim15":birim15,
            "birim16":birim16,
            "birim17":birim17,
            "birim18":birim18,
            "birim19":birim19,
            "birim20":birim20,
            "birim21":birim21,
        }

        
        index=1
        for birim in birims:
            context["birim"+str(index)].append(birims[index-1])
            index+=1


        index=1

        for birim in birims:
            turindex=0
            for tur in turs:
                
                sum=0
                toplam=0
            
                for ptnt in patentler:

                    if ptnt.tür==tur and ptnt.akademisyen.birim==birim:
                        sum+=1
                        ttur[turindex]+=sum

                turindex+=1
                context["birim"+str(index)].append(sum)
                toplam+=sum
                
            
            
            context["birim"+str(index)].append(toplam)
            index+=1
        
        turs.append("Toplam")

        
        return render(request,'patent rapor3.html',context)









def cikis_yap(request):
    oku = request.user.id
    if(not oku):
        return HttpResponseRedirect('/')
    logout(request)
    return HttpResponseRedirect('/')
