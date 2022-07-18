# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FQFkJ8l_vC07uB4hMa-tmMSuMWuTMlFH
"""

from asyncio import wait_for
def not_hesapla(satir):
   satir = satir[:-1]
   liste = satir.split(':')
   ogrenci_bilgiler = liste[0]
   not_durum = int(liste[1])
   
   if not_durum>=40 and not_durum<=100:
      durum = " Geçti"
   else:
      durum = " Kaldı"
    
   return ogrenci_bilgiler+ " :"+ durum + "\n"

def notlar():
  with open("sinav_notları.txt","r",encoding="UTF8") as file:
    for satir in file:
        print(not_hesapla(satir))

def notlar_gir():
  ad= input('Öğrencinin adı:')
  soyad= input('Öğrencinin soyadı:')
  numara= input('Öğrencinin numara:')
  not1= input('Öğrencinin not:')

  with open("sinav_notları.txt","a", encoding="UTF8) as file: 
   file.write(ad+' '+ soyad+' '+ numara+':'+not1+'\n')
def notlar_kaydet():
  with open('sinav_notları.txt',"r",encoding="UTF8") as file:  
   liste= []
   for i in file:
        liste.append(not_hesapla(i))
   with open("sonuclar.txt","w",encoding="UTF8") as file2:
        for i in liste:
            file2.write(i)   
while True:
  islem=input('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4-Çıkış\n')
  if islem == '1':
    notlar()
  elif islem == '2':
   notlar_gir()
  elif islem == '3':
    notlar_kaydet()
  else:
    break