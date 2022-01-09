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

#bu iki bos liste kadin ve erkek turkce notlari ayri ayri ayirlasin. 
turkce_K_notu = []
turkce_E_notu = []
#-------------------------------------------------------------------

# bunlar erkek ve kadin sayisi bir sayac 
sayi_K = 0
sayi_E = 0
#---------------------------------------

#kadin notlari
turkce_K = 0
matematik_K = 0
#erkek notlari
turkce_E = 0
matematik_E = 0


for i in range (len(sinav_sonucu["cinsiyet"])):
   # eger kadin sayaci +1
    if sinav_sonucu["cinsiyet"][i] =="K":
      sayi_K+=1
      turkce_K = turkce_K + sinav_sonucu["turkce"][i]
      matematik_K = matematik_K + sinav_sonucu["matematik"][i]
      #burda kadinlar turkce notu aliyor
      turkce_K_notu.append(sinav_sonucu["turkce"][i])
   # degilse erkek sayaci +1
    else:
      sayi_E+=1
      turkce_E = turkce_E + sinav_sonucu["turkce"][i]
      matematik_E = matematik_E + sinav_sonucu["matematik"][i]
      #burda erkekler turkce notu aliyor
      turkce_E_notu.append(sinav_sonucu["turkce"][i])


# suslu barantes icinde islem yapiyor
print(f"kandinlar matematik ort = {matematik_K/sayi_K}  \t\
Erkekler matematik ort = {matematik_E/sayi_E}   \t\
Turkce sinif ort = {(turkce_K + turkce_E) / (sayi_K + sayi_E)}")
# en yuksk notu aliyor
print("Kadin turkce max notu :" ,max(turkce_K_notu ))
print("Erkek turkce max notu :" ,max(turkce_E_notu ))

