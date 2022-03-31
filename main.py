KONUT_KADEME1_SU_TUKETIM = 2.89
KONUT_KADEME1_ATIK_SU= 1.44
KONUT_KADEME2_SU_TUKETIM = 3.13
KONUT_KADEME2_ATIK_SU = 1.56
KONUT_KADEME3_SU_TUKETIM = 6.43
KONUT_KADEME3_ATIK_SU = 3.22
ISYERI_SU_TUKETIM = 7.38
ISYERI_ATIK_SU= 3.68
RESMI_DAIRE_SU_TUKETIM = 4.34
RESMI_DAIRE_ATIK_SU = 2.16
ORGANIZE_SANAYI_SU_TUKETIM = 5
ORGANIZE_SANAYI_ATIK_SU = 2.5
ILCE_TARIMSAL_VE_HAYVAN_KADEME1_SU_TUKETIM = 1.45
ILCE_TARIMSAL_VE_HAYVAN_KADEME1_ATIK_SU = 0.72
ILCE_TARIMSAL_VE_HAYVAN_KADEME2_SU_TUKETIM = 2.89
ILCE_TARIMSAL_VE_HAYVAN_KADEME2_ATIK_SU = 1.44
ILCE_TARIMSAL_VE_HAYVAN_KADEME3_SU_TUKETIM = 6.43
ILCE_TARIMSAL_VE_HAYVAN_KADEME3_ATIK_SU = 3.22
CTV_TON_BASI = 0.39 #KDV SİZ
BORNOVA_BELEDIYE_KATI_ATIK_TOPLAMA_UCRETI= 13#KDVSİZ AYLIK HANE BASINA
BORNOVA_BELEDIYE_KATI_ATIK_BERTARAF_UCRETI = 2.54 #(HANE BASINA ) KDVDE YOK AYLIK
YUZDE_ELLI_INDIRIM = 0.5 # KONUT TIPI 1 İÇİN ŞEHİT,GAZİ,DEVLET SPORCUSU İÇİN GEÇERLİ
YUZDE_KIRK_ENGELLI = 0.5 # EN AZ YUZDE KIRK ENGELLI ICIN
SEHIT_GAZI_SPORCU_ABONELERI_SU_0_13=1.45
SEHIT_GAZI_SPORCU_ABONELERI_ATIK_0_13=0.72
SEHIT_GAZI_SPORCU_ABONELERI_ATIK_13_20=0.78
SEHIT_GAZI_SPORCU_ABONELERI_SU_13_20=1.57
SEHIT_GAZI_SPORCU_ABONELERI_ATIK_20=1.61
SEHIT_GAZI_SPORCU_ABONELERI_SU_20=3.22
ENGELLI_ABONE_SU_0_13=1.45
ENGELLI_ABONE_ATIK_0_13=0.72
ENGELLI_ABONE_SU_13_20=1.57
ENGELLI_ABONE_ATIK_13_20=0.78
ENGELLI_ABONE_ATIK_20=3.22
ENGELLI_ABONE_SU_20=6.43

def hane_sayi_al():

    print("Hane sayısını giriniz(Tam sayı) : ",end="")
    hane_sayi = int(input())
    while hane_sayi<0:
        print("Hatalı giriş. Hane sayısını tekrar giriniz(Tam sayı) : ", end="")
        hane_sayi = int(input())
    return hane_sayi

def sayac_degeri_hesaplama():
    print("Önceki sayaç değerini giriniz : ",end="")
    onceki_sayac_degeri = int(input())
    while onceki_sayac_degeri<0:
        print("Hatalı giriş. Önceki sayaç değerini tekrar giriniz : ", end="")
        onceki_sayac_degeri = int(input())
    print("Şimdiki sayaç değerini giriniz : ", end="")
    simdiki_sayac_degeri = int(input())
    while simdiki_sayac_degeri < onceki_sayac_degeri:
        print("Hatalı giriş. Şimdiki sayaç değerini tekrar giriniz : ", end="")
        simdiki_sayac_degeri = int(input())
    return simdiki_sayac_degeri-onceki_sayac_degeri

def gun_sayisi_giris():
    print("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz(Tam sayı) : ",end="")
    gun_sayisi = int(input())
    while gun_sayisi<0:
        print("Hatalı giriş. Lütfen önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını tekrar giriniz (Tam sayı) : ", end="")
        gun_sayisi = int(input())
    return gun_sayisi

def main():
    ozel_durum,hane_basina_ortalama_kullanim_miktari,kademe1,kademe2,kademe3,hane_sayi, isyeri_sayi, resmi_daire_sayi, organize_sanayi_sayi, ilce_tarimsal_sayi = 0,0, 0, 0, 0, 0, 0, 0, 0,0
    print("Abone no'nuzu giriniz : ",end="")
    abone_no = int(input())
    while abone_no<0:
        print("Hatalı giriş. Abone no'nuzu tekrar giriniz : ", end="")
        abone_no = int(input())
    print("Konut tipi 1 = Konut ")
    print("Konut tipi 2 = İşyeri ")
    print("Konut tipi 3 = Resmi Daire ")
    print("Konut tipi 4 = Organize Sanayi ")
    print("Konut tipi 5 = İlçe Tarımsal ve Hayvan Sulama ")

    print("Konut tipi giriniz(1 ile 5) : ",end="")
    konut_tipi = int(input())
    while konut_tipi<0 or konut_tipi>5:
        print("Hatalı giriş. Konut tipini tekrar giriniz(1 ile 5) : ", end="")
        konut_tipi = int(input())


    if konut_tipi==1:#konut kademe var
        hane_sayi=hane_sayi_al()

        if hane_sayi == 1:
            print("İndirim durumu var mı?,Yok/şehit/gazi/sporcu/engelli (y/Y/ş/Ş/g/G/s/S/e/E) : ", end="")
            indirim_durumu = input()
            while indirim_durumu not in ["y", "Y", "ş", "Ş", "g", "G", "s", "S", "E", "e"]:
                print("Yanlış girdiniz. Lütfen indirim durumunu tekrar giriniz, Yok/şehit/gazi/sporcu/engelli (y/Y/ş/Ş/g/G/s/S/e/E) : ",end="")
                indirim_durumu = input()
            kullanim_miktari = sayac_degeri_hesaplama()
            gun_sayisi = gun_sayisi_giris()

            if indirim_durumu in ["y","Y"]:
                if kullanim_miktari<=13:
                    su_tuketim_ucreti = (kullanim_miktari*KONUT_KADEME1_SU_TUKETIM)
                    atik_su_ucreti = (kullanim_miktari*KONUT_KADEME1_ATIK_SU)
                    kademe1=1
                elif kullanim_miktari >13 and kullanim_miktari <=20:
                    su_tuketim_ucreti = 13*KONUT_KADEME1_SU_TUKETIM+(kullanim_miktari-13)*KONUT_KADEME2_SU_TUKETIM
                    atik_su_ucreti = 13*KONUT_KADEME1_ATIK_SU+(kullanim_miktari-13)*KONUT_KADEME2_ATIK_SU
                    kademe2=1
                elif kullanim_miktari >20 :
                    su_tuketim_ucreti = 13 * KONUT_KADEME1_SU_TUKETIM + (7) * KONUT_KADEME2_SU_TUKETIM + KONUT_KADEME3_SU_TUKETIM*(kullanim_miktari-20)
                    atik_su_ucreti =13 * KONUT_KADEME1_ATIK_SU+7*KONUT_KADEME2_ATIK_SU+KONUT_KADEME3_ATIK_SU*(kullanim_miktari-20)
                    kademe3=1

            elif indirim_durumu in ["e","E"]:
                if kullanim_miktari<=13:
                    su_tuketim_ucreti = (kullanim_miktari*ENGELLI_ABONE_SU_0_13)
                    atik_su_ucreti = (kullanim_miktari*ENGELLI_ABONE_ATIK_0_13)
                    kademe1=1
                elif kullanim_miktari >13 and kullanim_miktari <=20:
                    su_tuketim_ucreti = 13*ENGELLI_ABONE_SU_0_13+(kullanim_miktari-13)*ENGELLI_ABONE_SU_13_20
                    atik_su_ucreti = 13*ENGELLI_ABONE_ATIK_0_13+(kullanim_miktari-13)*ENGELLI_ABONE_ATIK_13_20
                    kademe2 =1
                elif kullanim_miktari >20 :
                    su_tuketim_ucreti = 13 * ENGELLI_ABONE_SU_0_13 + (7) * ENGELLI_ABONE_SU_13_20 + ENGELLI_ABONE_SU_20*(kullanim_miktari-20)
                    atik_su_ucreti =13 * ENGELLI_ABONE_ATIK_0_13+7*ENGELLI_ABONE_ATIK_13_20+ENGELLI_ABONE_ATIK_20*(kullanim_miktari-20)
                    kademe3=1
                ozel_durum = 1
            elif indirim_durumu in ["ş", "Ş", "g", "G", "s", "S"]:
                if kullanim_miktari <= 13:
                    su_tuketim_ucreti = (kullanim_miktari * SEHIT_GAZI_SPORCU_ABONELERI_SU_0_13)
                    atik_su_ucreti = (kullanim_miktari * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_0_13)
                    kademe1=1
                elif kullanim_miktari > 13 and kullanim_miktari <= 20:
                    su_tuketim_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_SU_0_13 + (kullanim_miktari - 13) * SEHIT_GAZI_SPORCU_ABONELERI_SU_13_20
                    atik_su_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_0_13 + (kullanim_miktari - 13) * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_13_20
                    kademe2=1
                elif kullanim_miktari > 20:
                    su_tuketim_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_SU_0_13 + (7) * SEHIT_GAZI_SPORCU_ABONELERI_SU_13_20 + SEHIT_GAZI_SPORCU_ABONELERI_SU_20 * (kullanim_miktari - 20)
                    atik_su_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_0_13 + 7*SEHIT_GAZI_SPORCU_ABONELERI_ATIK_13_20 + SEHIT_GAZI_SPORCU_ABONELERI_ATIK_20 * (kullanim_miktari - 20)
                    kademe3=1
                ozel_durum = 1
            ctv_tutari=kullanim_miktari*CTV_TON_BASI



        else: # hane sayısını hane sayı al ile zaten 0 dan büyük oldugunu kontrol ettirdik.

            y=False
            while y==False:
                print("Şehit,gazi veya sporcu sayısını giriniz (0 ile", hane_sayi, "arasında) : ", end="")
                sehit_gazi_sporcu_sayisi = int(input())
                while sehit_gazi_sporcu_sayisi <0 or sehit_gazi_sporcu_sayisi > hane_sayi :
                    print("Hatalı giriş. Lütfen şehit,gazi veya sporcu sayısını tekrar giriniz (0 ile", hane_sayi,"arasında) : ", end="")
                    sehit_gazi_sporcu_sayisi = int(input())
                print("Engelli sayısını giriniz (0 ile", hane_sayi, "arasında) : ", end="")
                engelli_sayisi = int(input())
                while engelli_sayisi < 0 or engelli_sayisi > hane_sayi:
                    print("Hatalı giriş. Lütfen engelli sayısını tekrar giriniz (0 ile", hane_sayi, "arasında) : ", end="")
                    engelli_sayisi = int(input())
                if engelli_sayisi+sehit_gazi_sporcu_sayisi > hane_sayi:
                    print("Engelli sayısı ve şehit, gazi ve sporcu sayısının toplamı hane sayısından büyük cıktı. İşlemleri lütfen tekrar ediniz. ")
                else:
                    y = True
            ozel_durum = sehit_gazi_sporcu_sayisi+engelli_sayisi

            kullanim_miktari = sayac_degeri_hesaplama()
            gun_sayisi = gun_sayisi_giris()
            toplam_kullanim_miktari = kullanim_miktari#ısım kolaylasması ıcın bılerek farklı atama yapıyorum
            hane_basina_ortalama_kullanim_miktari = kullanim_miktari/hane_sayi
            normal_hane_sayisi = hane_sayi-engelli_sayisi-sehit_gazi_sporcu_sayisi
            kullanim_miktari = hane_basina_ortalama_kullanim_miktari#ısım kolaylasması ıcın bılerek farklı atama yapıyorum
            toplam_atik_su_ucreti = 0
            toplam_su_tuketim_ucreti=0
            if hane_basina_ortalama_kullanim_miktari <=13:
                kademe1=hane_sayi
            elif hane_basina_ortalama_kullanim_miktari <=20 and hane_basina_ortalama_kullanim_miktari >13:
                kademe2=hane_sayi
            elif hane_basina_ortalama_kullanim_miktari > 20:
                kademe3=hane_sayi

            if kullanim_miktari <= 13:
                su_tuketim_ucreti = (kullanim_miktari * KONUT_KADEME1_SU_TUKETIM)
                atik_su_ucreti = (kullanim_miktari * KONUT_KADEME1_ATIK_SU)
            elif kullanim_miktari > 13 and kullanim_miktari <= 20:
                su_tuketim_ucreti = 13 * KONUT_KADEME1_SU_TUKETIM + (kullanim_miktari - 13) * KONUT_KADEME2_SU_TUKETIM
                atik_su_ucreti = 13 * KONUT_KADEME1_ATIK_SU + (kullanim_miktari - 13) * KONUT_KADEME2_ATIK_SU

            elif kullanim_miktari > 20:
                su_tuketim_ucreti = 13 * KONUT_KADEME1_SU_TUKETIM + (7) * KONUT_KADEME2_SU_TUKETIM + KONUT_KADEME3_SU_TUKETIM * (kullanim_miktari - 20)
                atik_su_ucreti = 13 * KONUT_KADEME1_ATIK_SU + 7 * KONUT_KADEME2_ATIK_SU + KONUT_KADEME3_ATIK_SU * (kullanim_miktari - 20)
            toplam_atik_su_ucreti+=normal_hane_sayisi*atik_su_ucreti
            toplam_su_tuketim_ucreti+=normal_hane_sayisi*su_tuketim_ucreti

            if kullanim_miktari <= 13:
                su_tuketim_ucreti = (kullanim_miktari * ENGELLI_ABONE_SU_0_13)
                atik_su_ucreti = (kullanim_miktari * ENGELLI_ABONE_ATIK_0_13)

            elif kullanim_miktari > 13 and kullanim_miktari <= 20:
                su_tuketim_ucreti = 13 * ENGELLI_ABONE_SU_0_13 + (kullanim_miktari - 13) * ENGELLI_ABONE_SU_13_20
                atik_su_ucreti = 13 * ENGELLI_ABONE_ATIK_0_13 + (kullanim_miktari - 13) * ENGELLI_ABONE_ATIK_13_20

            elif kullanim_miktari > 20:
                su_tuketim_ucreti = 13 * ENGELLI_ABONE_SU_0_13 + (7) * ENGELLI_ABONE_SU_13_20 + ENGELLI_ABONE_SU_20 * (kullanim_miktari - 20)
                atik_su_ucreti = 13 * ENGELLI_ABONE_ATIK_0_13 + 7 * ENGELLI_ABONE_ATIK_13_20 + ENGELLI_ABONE_ATIK_20 * (kullanim_miktari - 20)

            toplam_su_tuketim_ucreti+=engelli_sayisi*su_tuketim_ucreti
            toplam_atik_su_ucreti+=engelli_sayisi*atik_su_ucreti

            if kullanim_miktari <= 13:
                su_tuketim_ucreti = (kullanim_miktari * SEHIT_GAZI_SPORCU_ABONELERI_SU_0_13)
                atik_su_ucreti = (kullanim_miktari * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_0_13)

            elif kullanim_miktari > 13 and kullanim_miktari <= 20:
                su_tuketim_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_SU_0_13 + (kullanim_miktari - 13) * SEHIT_GAZI_SPORCU_ABONELERI_SU_13_20
                atik_su_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_0_13 + (kullanim_miktari - 13) * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_13_20

            elif kullanim_miktari > 20:
                su_tuketim_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_SU_0_13 + (7) * SEHIT_GAZI_SPORCU_ABONELERI_SU_13_20 + SEHIT_GAZI_SPORCU_ABONELERI_SU_20 * (kullanim_miktari - 20)
                atik_su_ucreti = 13 * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_0_13 + 7 * SEHIT_GAZI_SPORCU_ABONELERI_ATIK_13_20 + SEHIT_GAZI_SPORCU_ABONELERI_ATIK_20 * (kullanim_miktari - 20)

            toplam_atik_su_ucreti+=sehit_gazi_sporcu_sayisi*atik_su_ucreti
            toplam_su_tuketim_ucreti+=sehit_gazi_sporcu_sayisi*su_tuketim_ucreti

            su_tuketim_ucreti = toplam_su_tuketim_ucreti
            atik_su_ucreti = toplam_atik_su_ucreti
            kullanim_miktari = toplam_kullanim_miktari#ısım kolaylasması ıcın bılerek farklı atama yapıyorum
            ctv_tutari = kullanim_miktari*CTV_TON_BASI

        konut_tipi="Konut"





    elif konut_tipi==2:#isyeri kademe yok
        kullanim_miktari = sayac_degeri_hesaplama()
        gun_sayisi = gun_sayisi_giris()
        su_tuketim_ucreti = (kullanim_miktari * ISYERI_SU_TUKETIM)
        atik_su_ucreti = (kullanim_miktari * ISYERI_ATIK_SU)
        ctv_tutari = kullanim_miktari*CTV_TON_BASI
        konut_tipi="İşyeri"
        isyeri_sayi = 1


    elif konut_tipi ==3:#resmi daire kademe yok
        kullanim_miktari = sayac_degeri_hesaplama()
        gun_sayisi = gun_sayisi_giris()
        su_tuketim_ucreti = (kullanim_miktari * RESMI_DAIRE_SU_TUKETIM)
        atik_su_ucreti = (kullanim_miktari * RESMI_DAIRE_ATIK_SU)
        ctv_tutari = kullanim_miktari * CTV_TON_BASI
        konut_tipi="Resmi Daire"
        resmi_daire_sayi = 1

    elif konut_tipi==4: # organize sanayi kademe yok
        kullanim_miktari = sayac_degeri_hesaplama()
        gun_sayisi = gun_sayisi_giris()
        su_tuketim_ucreti = (kullanim_miktari * ORGANIZE_SANAYI_SU_TUKETIM)
        atik_su_ucreti = (kullanim_miktari * ORGANIZE_SANAYI_ATIK_SU)
        ctv_tutari = kullanim_miktari * CTV_TON_BASI
        konut_tipi = "Organize Sanayi"
        organize_sanayi_sayi = 1

    elif konut_tipi==5:# ilçe tarımsal ve hayvan sulama 3 kademe var
        kullanim_miktari = sayac_degeri_hesaplama()
        gun_sayisi = gun_sayisi_giris()
        if kullanim_miktari <= 13:
            su_tuketim_ucreti = (kullanim_miktari * ILCE_TARIMSAL_VE_HAYVAN_KADEME1_SU_TUKETIM)
            atik_su_ucreti = (kullanim_miktari * ILCE_TARIMSAL_VE_HAYVAN_KADEME1_ATIK_SU)

        elif kullanim_miktari > 13 and kullanim_miktari <= 20:
            su_tuketim_ucreti = 13 * ILCE_TARIMSAL_VE_HAYVAN_KADEME1_SU_TUKETIM + (kullanim_miktari - 13) * ILCE_TARIMSAL_VE_HAYVAN_KADEME2_SU_TUKETIM
            atik_su_ucreti = 13 * ILCE_TARIMSAL_VE_HAYVAN_KADEME1_ATIK_SU + (kullanim_miktari - 13) * ILCE_TARIMSAL_VE_HAYVAN_KADEME2_ATIK_SU

        elif kullanim_miktari > 20:
            su_tuketim_ucreti = 13 * ILCE_TARIMSAL_VE_HAYVAN_KADEME1_SU_TUKETIM + (7) * ILCE_TARIMSAL_VE_HAYVAN_KADEME2_SU_TUKETIM + ILCE_TARIMSAL_VE_HAYVAN_KADEME3_SU_TUKETIM * (kullanim_miktari - 20)
            atik_su_ucreti = 13 * ILCE_TARIMSAL_VE_HAYVAN_KADEME1_ATIK_SU + 7 * ILCE_TARIMSAL_VE_HAYVAN_KADEME2_ATIK_SU + ILCE_TARIMSAL_VE_HAYVAN_KADEME3_ATIK_SU * (kullanim_miktari - 20)

        konut_tipi="İlçe Tarımsal ve Hayvan Sulama"
        ilce_tarimsal_sayi = 1
        ctv_tutari = kullanim_miktari*CTV_TON_BASI

    if hane_sayi==0:
        belediye_kati_atik_toplama = BORNOVA_BELEDIYE_KATI_ATIK_TOPLAMA_UCRETI
        belediye_kati_atik_bertaraf = BORNOVA_BELEDIYE_KATI_ATIK_BERTARAF_UCRETI
    elif hane_sayi>0:
        belediye_kati_atik_toplama = BORNOVA_BELEDIYE_KATI_ATIK_TOPLAMA_UCRETI*hane_sayi
        belediye_kati_atik_bertaraf = BORNOVA_BELEDIYE_KATI_ATIK_BERTARAF_UCRETI*hane_sayi
    kdv_tutari=(su_tuketim_ucreti+atik_su_ucreti+(belediye_kati_atik_bertaraf)+(belediye_kati_atik_toplama))*0.08
    toplam_tutar= ctv_tutari+(kdv_tutari)*100/8+kdv_tutari
    devlet_geliri = kdv_tutari
    ilce_belediye_geliri=ctv_tutari+belediye_kati_atik_toplama
    buyuk_sehir_geliri=belediye_kati_atik_bertaraf
    izsu_geliri = toplam_tutar-ctv_tutari-kdv_tutari-(belediye_kati_atik_bertaraf)-(belediye_kati_atik_toplama)

    print("Abone no : ", abone_no)
    print("Abone tipi adı : ",konut_tipi)
    print("Dönemlik su tüketim miktarı : ",format(kullanim_miktari,".2f"))
    print("Dönemlik su tüketim ücreti : ",format(su_tuketim_ucreti,".2f"))
    print("Dönemlik atık su ücreti : ",format(atik_su_ucreti,".2f"))
    print("Dönemlik toplam su tüketim ve atık su ücreti : ", format(su_tuketim_ucreti+atik_su_ucreti,".2f"))
    print("Dönemlik CTV tutarı : ",format(ctv_tutari,".2f"))
    print("Dönemlik katı atık toplama ücreti :", format(belediye_kati_atik_toplama,".2f"))
    print("Dönemlik katı atık bertaraf ücreti : ", format(belediye_kati_atik_bertaraf,".2f"))
    print("Dönemlik toplam fatura tutarı :", format(toplam_tutar,".2f"))
    print("Dönemlik devlete aktarılıcak KDV tutarı(%8) : ",format(kdv_tutari,".2f"))
    print("Dönemlik ilçe belediyesine aktarılacak tutar(katı atık toplama + çtv) : ", format((belediye_kati_atik_toplama + ctv_tutari),".2f"))
    print("Dönemlik büyük şehir belediyesine aktarılacak tutar(bertaraf) : ",format((belediye_kati_atik_bertaraf),".2f"))
    print("Dönemlik İZSU payı : ", format((toplam_tutar-ctv_tutari-kdv_tutari-(belediye_kati_atik_bertaraf)-(belediye_kati_atik_toplama)),".2f"))

    return su_tuketim_ucreti,ozel_durum,izsu_geliri,buyuk_sehir_geliri,ilce_belediye_geliri,devlet_geliri,konut_tipi,hane_basina_ortalama_kullanim_miktari,kademe1,kademe2,kademe3,abone_no,hane_sayi,isyeri_sayi,resmi_daire_sayi,organize_sanayi_sayi,ilce_tarimsal_sayi,kullanim_miktari,toplam_tutar,gun_sayisi

konut_abonesi=0
isyeri_abonesi=0
resmi_daire_abonesi=0
organize_sanayi_abonesi=0
ilce_tarimsal_abonesi=0
toplam_hane_su_tuketim  = 0
toplam_isyeri_su_tuketim=0
toplam_resmi_daire_su_tuketim=0
toplam_organize_sanayi_su_tuketim=0
toplam_ilce_tarimsal_su_tuketim=0
cok_para_veren_sayisi = 0
aylik_toplam_konut_tipi_su_tuketim =0
aylik_toplam_isyeri_tipi_su_tuketim =0
aylik_toplam_resmi_daire_tipi_su_tuketim =0
aylik_toplam_organize_sanayi_tipi_su_tuketim =0
aylik_toplam_ilce_tarimsal_tipi_su_tuketim =0
kademe1_kullanici_sayisi=0
kademe2_kullanici_sayisi=0
kademe3_kullanici_sayisi=0
aylik_ortalama_kademe1_su_tuketim =0
aylik_ortalama_kademe2_su_tuketim =0
aylik_ortalama_kademe3_su_tuketim =0
toplam_ilce_tarimsal_su_tuketimi_elliden_fazla =0
resmi_daire_en_yuksek_tuketim_abone_no = 0
resmi_daire_en_yuksek_tuketim_miktari = 0
aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_ucreti =0
aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_abone_no = 0
aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_abone_tipi = ""
aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_kulandigi_miktar = 0
konut_tipi_aylik_su_tuketim_ucreti=0
isyeri_tipi_aylik_su_tuketim_ucreti=0
organize_sanayi_tipi_aylik_su_tuketim_ucreti=0
resmi_daire_tipi_aylik_su_tuketim_ucreti=0
ilce_tarimsal_tipi_aylik_su_tuketim_ucreti=0
izsu_geliri_toplam,buyuk_sehir_geliri_toplam,ilce_belediye_geliri_toplam,devlet_geliri_toplam=0,0,0,0
toplam_ozel_durumlu_sayisi=0

x = True
while x == True:

    su_tuketim_ucreti,ozel_durum,izsu_geliri,buyuk_sehir_geliri,ilce_belediye_geliri,devlet_geliri,konut_tipi,hane_basina_ortalama_kullanim_miktari,kademe1,kademe2,kademe3,abone_no,hane_sayi,isyeri_sayi,resmi_daire_sayi,organize_sanayi_sayi,ilce_tarimsal_sayi,kullanim_miktari,toplam_tutar,gun_sayisi = main()
    konut_abonesi += hane_sayi
    isyeri_abonesi += isyeri_sayi
    resmi_daire_abonesi += resmi_daire_sayi
    organize_sanayi_abonesi += organize_sanayi_sayi
    ilce_tarimsal_abonesi += ilce_tarimsal_sayi
    izsu_geliri_toplam+=izsu_geliri
    buyuk_sehir_geliri_toplam+=buyuk_sehir_geliri
    ilce_belediye_geliri_toplam+=ilce_belediye_geliri
    devlet_geliri_toplam+=devlet_geliri

    toplam_ozel_durumlu_sayisi+=ozel_durum

    if hane_sayi==0:
        if aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_ucreti<(su_tuketim_ucreti)/(gun_sayisi)*30:
            aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_ucreti = (su_tuketim_ucreti)/(gun_sayisi)*30
            aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_abone_no = abone_no
            aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_abone_tipi = konut_tipi
            aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_kulandigi_miktar = (kullanim_miktari)/(gun_sayisi)*30
    if kademe1 >0:
        kademe1_kullanici_sayisi+=kademe1
        aylik_ortalama_kademe1_su_tuketim += kullanim_miktari / (gun_sayisi)*30
    elif kademe2>0:
        kademe2_kullanici_sayisi += kademe2
        aylik_ortalama_kademe2_su_tuketim += kullanim_miktari / (gun_sayisi)*30
    elif kademe3>0:

        kademe3_kullanici_sayisi += kademe3
        aylik_ortalama_kademe3_su_tuketim += kullanim_miktari / (gun_sayisi)*30


    if hane_sayi>0 :
        toplam_hane_su_tuketim += kullanim_miktari
        aylik_toplam_konut_tipi_su_tuketim += (kullanim_miktari/gun_sayisi)*30
        konut_tipi_aylik_su_tuketim_ucreti+=(su_tuketim_ucreti/gun_sayisi)*30
    elif isyeri_sayi >0:
        toplam_isyeri_su_tuketim += kullanim_miktari
        aylik_toplam_isyeri_tipi_su_tuketim+= (kullanim_miktari/gun_sayisi)*30
        isyeri_tipi_aylik_su_tuketim_ucreti += (su_tuketim_ucreti)/(gun_sayisi)*30
    elif resmi_daire_sayi >0:
        toplam_resmi_daire_su_tuketim += kullanim_miktari
        aylik_toplam_resmi_daire_tipi_su_tuketim += (kullanim_miktari/gun_sayisi)*30
        resmi_daire_tipi_aylik_su_tuketim_ucreti += (su_tuketim_ucreti)/(gun_sayisi)*30
        if resmi_daire_en_yuksek_tuketim_miktari<(kullanim_miktari)/(gun_sayisi)*30:
            resmi_daire_en_yuksek_tuketim_miktari = (kullanim_miktari)/(gun_sayisi)*30
            resmi_daire_en_yuksek_tuketim_abone_no = abone_no
    elif organize_sanayi_sayi>0:
        toplam_organize_sanayi_su_tuketim += kullanim_miktari
        aylik_toplam_organize_sanayi_tipi_su_tuketim+= (kullanim_miktari/gun_sayisi)*30
        organize_sanayi_tipi_aylik_su_tuketim_ucreti += (su_tuketim_ucreti)/(gun_sayisi)*30
    elif ilce_tarimsal_sayi>0:
        toplam_ilce_tarimsal_su_tuketim += kullanim_miktari
        aylik_toplam_ilce_tarimsal_tipi_su_tuketim+= (kullanim_miktari/gun_sayisi)*30
        ilce_tarimsal_tipi_aylik_su_tuketim_ucreti += (su_tuketim_ucreti)/(gun_sayisi)*30
        if 30*(kullanim_miktari/gun_sayisi)>50:
            toplam_ilce_tarimsal_su_tuketimi_elliden_fazla +=1

    if hane_sayi>1:
        if (hane_basina_ortalama_kullanim_miktari/(gun_sayisi)*30)>100 or (su_tuketim_ucreti/(gun_sayisi)*30)/(hane_sayi) >500:
            cok_para_veren_sayisi += hane_sayi

    elif ((kullanim_miktari)/(gun_sayisi)*30) >100 or (su_tuketim_ucreti/(gun_sayisi)*30) >500:
        if hane_sayi ==1 or isyeri_sayi==1 or resmi_daire_sayi==1 or organize_sanayi_sayi==1 or ilce_tarimsal_sayi==1:
            cok_para_veren_sayisi += 1

    devam=input("Başka abone var mı?(e/E/h/H) : ")
    while devam not in ["e","E","h","H"]:
        devam = input("Hatalı giriş. Başka abone var mı?(e/E/h/H) : ")
    if devam in ["h","H"]:
        x=False


print("Konut abone sayisi : ",konut_abonesi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ", format(((konut_abonesi)/(konut_abonesi+isyeri_abonesi+resmi_daire_abonesi+organize_sanayi_abonesi+ilce_tarimsal_abonesi)*100),".2f") ,  end="")
print(" Aylık ortalama su tüketimi : ",format((aylik_toplam_konut_tipi_su_tuketim/(konut_abonesi)),".2f"))
print("İşyeri abone sayisi : ",isyeri_abonesi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ", format((isyeri_abonesi)/(konut_abonesi+isyeri_abonesi+resmi_daire_abonesi+organize_sanayi_abonesi+ilce_tarimsal_abonesi)*100,".2f"),end="")
print(" Aylık ortalama su tüketimi : ", format((aylik_toplam_isyeri_tipi_su_tuketim/(isyeri_abonesi)),".2f"))
print("Resmi daire abone sayisi : ",resmi_daire_abonesi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ", format((resmi_daire_abonesi)/(konut_abonesi+isyeri_abonesi+resmi_daire_abonesi+organize_sanayi_abonesi+ilce_tarimsal_abonesi)*100,".2f"),end="")
print(" Aylık ortalama su tüketimi : ",format(aylik_toplam_resmi_daire_tipi_su_tuketim/(resmi_daire_abonesi),".2f"))
print("Organize sanayi abone sayısı : ",organize_sanayi_abonesi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ",format((organize_sanayi_abonesi)/(konut_abonesi+isyeri_abonesi+resmi_daire_abonesi+organize_sanayi_abonesi+ilce_tarimsal_abonesi)*100,".2f"),end="")
print(" Aylık ortalama su tüketimi : ",format(aylik_toplam_organize_sanayi_tipi_su_tuketim/(organize_sanayi_abonesi),".2f"))
print("İlçe tarımsal ve hayvan sulama abonesi : ",ilce_tarimsal_abonesi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ", format((ilce_tarimsal_abonesi)/(konut_abonesi+isyeri_abonesi+resmi_daire_abonesi+organize_sanayi_abonesi+ilce_tarimsal_abonesi)*100,".2f"),end="")
print(" Aylık ortalama su tüketimi : ",format(aylik_toplam_ilce_tarimsal_tipi_su_tuketim/(ilce_tarimsal_abonesi),".2f"))


print("Kademesi bir olan abone sayisi : ",kademe1_kullanici_sayisi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ",format((kademe1_kullanici_sayisi)/(kademe1_kullanici_sayisi+kademe2_kullanici_sayisi+kademe3_kullanici_sayisi)*100,".2f"), end="")
print(" Aylık ortalama su tüketimi : ",format((aylik_ortalama_kademe1_su_tuketim/kademe1_kullanici_sayisi),".2f"))

print("Kademesi iki olan abone sayisi : ",kademe2_kullanici_sayisi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ",format(kademe2_kullanici_sayisi/(kademe1_kullanici_sayisi+kademe2_kullanici_sayisi+kademe3_kullanici_sayisi)*100,".2f"),end="")
print(" Aylık ortalama su tüketimi : ",format((aylik_ortalama_kademe2_su_tuketim/kademe2_kullanici_sayisi),".2f"))

print("Kademesi üç olan abone sayisi : ",kademe3_kullanici_sayisi,end="")
print(" Ve tüm aboneler icindeki yüzdesi : ",format(kademe3_kullanici_sayisi/(kademe1_kullanici_sayisi+kademe2_kullanici_sayisi+kademe3_kullanici_sayisi)*100,".2f"), end="")
print(" Aylık ortalama su tüketimi : ", format(aylik_ortalama_kademe3_su_tuketim/kademe3_kullanici_sayisi,".2f"))


print("Aylık su tüketim miktarı elli tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı : ",toplam_ilce_tarimsal_su_tuketimi_elliden_fazla,end="")
print(" veilçe tarımsal ve hayvan sulama tipi abonelerin içindeki yüzdesi : ",format(toplam_ilce_tarimsal_su_tuketimi_elliden_fazla/ilce_tarimsal_abonesi*100,".2f"))

print("Aylık su tüketim miktarı 100 tondan yuksek veya aylık su tüketim ücreti 500 liradan yüksek olan abonelerin sayısı : ",cok_para_veren_sayisi)

print("Şehit,gazi veya devlet sporcusu olan ve engelli olan konut tipi abonelerin(hanelerin) sayısı :",toplam_ozel_durumlu_sayisi,end="" )
print(" Ve konut tipi aboneler içindeki yüzdesi : ",format(toplam_ozel_durumlu_sayisi/konut_abonesi*100,".2f"))

print("Aylık su tüketim miktarı en yüksek olan resimi daire tipi abonenin abone numarası : ",resmi_daire_en_yuksek_tuketim_abone_no,end="")
print(" Ve aylık su tüketim miktarı : ",format(resmi_daire_en_yuksek_tuketim_miktari,".2f"))

print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no'su, : ",aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_abone_no ,end="")
print(" Abone tipi adı : ",aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_abone_tipi,end="")
print(" Aylık su tüketim miktarı : ",format(aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_kulandigi_miktar,".2f"),end="")
print(" Ve ödediği aylık su tüketim ücreti : ",format(aylik_su_tuketim_ucreti_en_yuksek_olan_abonenin_ucreti,".2f"))

bornovanin_aylik_toplam_su_tuketim_miktari=aylik_toplam_ilce_tarimsal_tipi_su_tuketim+aylik_toplam_organize_sanayi_tipi_su_tuketim+aylik_toplam_resmi_daire_tipi_su_tuketim+aylik_toplam_isyeri_tipi_su_tuketim+aylik_toplam_konut_tipi_su_tuketim

print("Konut tipi için aylık toplam su tüketim miktarı, :",format(aylik_toplam_konut_tipi_su_tuketim,".2f"),end="")
print(" Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(aylik_toplam_konut_tipi_su_tuketim/bornovanin_aylik_toplam_su_tuketim_miktari*100,".2f"))
print("İşyeri tipi için aylık toplam su tüketim miktarı, :",format(aylik_toplam_isyeri_tipi_su_tuketim,".2f"),end="")
print(" Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(aylik_toplam_isyeri_tipi_su_tuketim/bornovanin_aylik_toplam_su_tuketim_miktari*100,".2f"))
print("Resmi Daire tipi için aylık toplam su tüketim miktarı, :",format(aylik_toplam_resmi_daire_tipi_su_tuketim,".2f"),end="")
print(" Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(aylik_toplam_resmi_daire_tipi_su_tuketim/bornovanin_aylik_toplam_su_tuketim_miktari*100,".2f"))
print("Organize sanayi tipi için aylık toplam su tüketim miktarı, :",format(aylik_toplam_organize_sanayi_tipi_su_tuketim,".2f"),end="")
print(" Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(aylik_toplam_organize_sanayi_tipi_su_tuketim/bornovanin_aylik_toplam_su_tuketim_miktari*100,".2f"))
print("İlçe tarımsal ve hayvan sulama tipi için aylık toplam su tüketim miktarı, :",format(aylik_toplam_ilce_tarimsal_tipi_su_tuketim,".2f"),end="")
print(" Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi : ",format(aylik_toplam_ilce_tarimsal_tipi_su_tuketim/bornovanin_aylik_toplam_su_tuketim_miktari*100,".2f"))
print("Bornova'nın aylık toplam su tüketim miktarı : ", format(bornovanin_aylik_toplam_su_tuketim_miktari,".2f"))

print("Konut tipi için elde edilen aylık toplam su tüketim ücreti",format(konut_tipi_aylik_su_tuketim_ucreti,".2f"))
print("İşyeri tipi için elde edilen aylık toplam su tüketim ücreti",format(isyeri_tipi_aylik_su_tuketim_ucreti,".2f"))
print("Resmi daire tipi için elde edilen aylık toplam su tüketim ücreti",format(resmi_daire_tipi_aylik_su_tuketim_ucreti,".2f"))
print("Organize sanayi tipi için elde edilen aylık toplam su tüketim ücreti",format(organize_sanayi_tipi_aylik_su_tuketim_ucreti,".2f"))
print("Tarım ve hayvansal sulama tipi için elde edilen aylık toplam su tüketim ücreti",format(ilce_tarimsal_tipi_aylik_su_tuketim_ucreti,".2f"))
print("Tüm abonelerden elde edilen aylık toplam su tüketim ücreti : ",format(konut_tipi_aylik_su_tuketim_ucreti+isyeri_tipi_aylik_su_tuketim_ucreti+resmi_daire_tipi_aylik_su_tuketim_ucreti+organize_sanayi_tipi_aylik_su_tuketim_ucreti+ilce_tarimsal_tipi_aylik_su_tuketim_ucreti,".2f"))

print("İlgili dönemde su faturalarından İZSU'nun elde ettiği gelir tutarı : ",format(izsu_geliri_toplam,".2f"))
print("İlgili dönemde su faturalarından ilçe belediyesinin elde ettiği gelir tutarı : ",format(ilce_belediye_geliri_toplam,".2f"))
print("İlgili dönemde su faturalarından büyükşehir belediyesinin elde ettiği gelir tutarı : ",format(buyuk_sehir_geliri_toplam,".2f"))
print("İlgili dönemde su faturalarından devletin elde ettiği gelir tutarı : ",format(devlet_geliri_toplam,".2f"))

