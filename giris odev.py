#1 liste olusturdum
kisiler = ["mohamad" , "ghaith" , "omer" , "amir" ]
kulancilist = []
#2 liste ekrana yazdir
print(kisiler)


j =int(input("kac isim eklemek istiyorsun   :  "))
#3 kulancidan 3 isim iste
for i in range (j): 
 kulancilist = input("Enter the names  :  ")


#4 kulanc girdiği isim listeye ekleyiniz ve ekrana yazdir
 kisiler.append(kulancilist)
 print(kisiler)

#5 liste uzunluğu

print(len(kisiler))

#6 Listenin 2. elemanını ekrana yazdırınız
print(kisiler[1])

#7 son elemanını listeden sil
kisiler.pop(-1)

for i in range (len(kisiler)) :  
 print(kisiler[i])
