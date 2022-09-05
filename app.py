# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:20:21 2021

@author: Marshel
"""
import numpy as np #import library numpy 
import time #import library time
import random #import library random

kata1 = np.array(["ya","wali","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan"
,"aku","dia","mereka","kita","tidak","baik","bodoh","pintar","suka","udara","waktu","presiden","jadi",
"daring","uang","duit","korupsi","desa","kota","hilang","pergi","datang","waktu","acak","rumah","atap",
"kaca","cermin","lilin","korek","asap","kipas","angin","jaket","baju","kemeja","kaos","anjing","kucing",
"angka","hotel","warung","buku","pulpen","pensil","mobil","sepeda","kail","ikan","semut","umpan","kulkas",
"burung","pakan","ayam","mamalia","unggas","angsa","bebek","internet","komputer","telepon","pantai",
"siap","jiwa","roh","tubuh","fisik","nasi","tahu","kami","mata","akan","terjadi","air","bagian",
"pergi","kembali","raga","olah","pulang","mampu","cara","kerja","apa","mengapa","dimana","siapa",
"kapan","bagaimana","dan","di","ke","bank","api","jam","berapa","ini","itu","selama","kepada","tulang"]) #array yang berfungsi untuk menyimpan kata - kata berbahasa Indonesia
                                                                                                        
kata2 = np.array(["yes","guardian","one","two","three","four","five","six","seven","eight","nine"
,"me","he","they","we","no","bad","stupid","clever","like","air","time","president","well",
"online","money","wrench","corruption","village","city","disappear","gone","come","time","random","house","ceiling",
"glass","miror","candle","matches","smoke","fan","wind","jacket","clothes","shirt","swim","dog","cat",
"number","hotel","shop","book","pen","pencil","car","bicycle","hook","fish","ant","bait","refrigerator",
"bird","feed","chicken","mammal","poultry","goose","duck","internet","computer","telephone","beach",
"ready","soul","spirit","body","physical","rice","tofu","our","eye","will","happen","water","section",
"leave","return","obsidian","manner","desk","capable","method","activity","what","why","where","who",
"when","how","and","at","to","bank","fire","clock","helm","this","that","during","mask","boxing"]) #array yang berfungsi untuk menyimpan kata - kata berbahasa inggris
                                                                                                    
random.shuffle(kata1) #untuk merandom array yang sudah dibuat dalam bahasa Indonesia
random.shuffle(kata2) #untuk merandom array yang sudah dibuat dalam bahasa inggris
benar = 0 #variable untuk menghitung akurasi
salah = 0 #variable untuk menghitung akurasi
print ("Selamat datang di Aplikasi SpeedTyping")
print ("Silahkan pilih bahasa pengetikan : ")
print ("1. Indonesia") #pilihan bahasa
print ("2. English") #pilihan bahasa
print (" Pilih?(INPUT ANGKA!)") 
pilih = int(input()) #inputan untuk memilih bahasa

if pilih == 1:  #jika user memilih angka 1 berarti user ingin mengetik dalam bahasa Indonesia
    
    print("Anda akan mengetik 65 kata dalam waktu sesingkat-singkatnya, usahakan anda tidak membuat kesalahan!")#Petunjuk untuk user
    print("65 kata tersebut akan ditampilkan dalam bentuk paragraf, ketikkan paragraf tersebut tanpa menggunakan ENTER!") 
    print("Jika paragraf selesai dibuat, tekan ENTER untuk mengakhiri!")
    print("Jika sudah siap, tekan ENTER untuk memulai!")    #Akhir dari petunjuk penggunaan aplikasi
    input()
    print()

    for i in range(0,65): #menampilkan 65 kata dari array kata1
        print(kata1[i],end=' ')
    print()
        
    mulai = time.time() #mulai menghitung waktu dari line ini
    ketik=input()
    akhir = time.time() #berhenti menghitung waktu sampai line ini
    ketik = ketik.split() #mengubah string "ketik" menjadi sebuah list berisi kata-kata yang diketik
        
    try:
        for i in range(0,65): #looping mengecek kecocokan kata
            if ketik[i]==kata1[i]:
                benar+=1
            else:
                salah+=1
                    
        akurasi = (benar/65)*100 #rumus menghitung akurasi 
        print ("\nAkurasi : %3.2f%%" % (akurasi)) #menampilkan akurasi
        waktu = akhir-mulai #menghitung total waktu yang diperlukan dari line 
        kpmgross = 65/(waktu/60) #untuk menghitung kpmbersih
        kpmbersih = kpmgross-(salah/(waktu/60)) #untuk menghitung KPM user
        print("KPM : %d kata per menit" % (kpmbersih)) #menampilkan KPM user
                    
    except:
        print("Error! Kata-kata yang anda tuliskan kurang/lebih dari 65 kata ! Silahkan ulangi program!") #Error Handling

elif pilih == 2:   #jika user memilih angka 2 berarti user ingin mengetik dalam bahasa Inggris
    print("You will be typing 65 words in the shortest possible time, try not to make any mistakes!")
    print("The 65 words will be displayed in paragraph form, type the paragraph without using ENTER!") 
    print("If paragraphs are finished, press ENTER to end!")
    print("If you are ready press ENTER to start")  #petunjuk penggunaan aplikasi
    input()
    print()
    for i in range(0,65): #menampilkan 65 kata dari array kata2
        print(kata2[i],end=' ')
    print()
        
    mulai = time.time() #mulai menghitung waktu dari line ini
    ketik=input() 
    akhir = time.time() #berhenti menghitung waktu sampai line ini
    ketik = ketik.split() #mengubah string "ketik" menjadi sebuah list berisi kata-kata yang diketik
        
    try:
        for i in range(0,65): #looping mengecek kecocokan kata yang diketik
            if ketik[i]==kata2[i]:
                benar+=1
            else:
                salah+=1
                    
        akurasi = (benar/65)*100 #rumus menghitung akurasi 
        print ("\nAccuracy : %3.2f%%" % (akurasi)) #menampilkan akurasi
        waktu = akhir-mulai #menghitung total waktu yang diperlukan dari line 
        kpmgross = 65/(waktu/60) #untuk menghitung kpmbersih
        kpmbersih = kpmgross-(salah/(waktu/60)) #untuk menghitung WPM user
        print("WPM : %d Word per minute" % (kpmbersih)) #menampilkan WPM user
                
    except:
        print("Error! The word you type less than 65 word or more! Please repeate the program!") #Error Handling