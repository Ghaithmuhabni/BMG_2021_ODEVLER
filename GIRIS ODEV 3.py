# adi ve soyadi : mohamad ghaith muhbani
#?<NO:21080410033>


# ana liste
sinav_sonucu =  {'name':["ayse", "ahmet", "nuri" , "nawar", "suzan", "ala"] ,
 "cinsiyet":["K" , "E" , "E" , "E" , "K" ,"K"] , 
  "matematik":[60 , 40  , 97 , 45 , 56 , 95],
   "turkce":[70 , 30 , 23 , 80 , 78 , 46] }

print(sinav_sonucu['name'])
print(sinav_sonucu['cinsiyet'])
print(sinav_sonucu['matematik'])
print(sinav_sonucu['turkce'])

def yeni_kayit () :


   yeni_cinsiyet  = []
   yeni_mat_not   = []
   yeni_turkc_not = []
   yeni_isim      = [] 


   for i in range (2):
      isim =(input("isim giriniz : "))
      cinsiyet =(input("cinsiyet giriniz : "))
      mat_notu =(input("matematik notu giriniz : "))
      turkc_notu =(input("turkce notu giriniz : "))

      yeni_isim.append(isim)
      yeni_cinsiyet.append(cinsiyet)
      yeni_mat_not.append(mat_notu)
      yeni_turkc_not.append(turkc_notu)

      print(yeni_isim)
      print(yeni_cinsiyet)
      print(yeni_mat_not)
      print(yeni_turkc_not)


      sinav_sonucu["name"].append(yeni_isim[i])
      sinav_sonucu["cinsiyet"].append(yeni_cinsiyet[i])
      sinav_sonucu["matematik"].append(yeni_mat_not[i])
      sinav_sonucu["turkce"].append(yeni_turkc_not[i])



   print(sinav_sonucu['name'])
   print(sinav_sonucu['cinsiyet'])
   print(sinav_sonucu['matematik'])
   print(sinav_sonucu['turkce'])

yeni_kayit()