'''
PROGRAM MENGECEK TOTAL HARGA PRINTER
NI PUTU DEWI LESTARI (20083000137)
KELAS 2-F
'''
import os
clear = lambda : os.system('cls')

jwb = "y"
while jwb == "y" or jwb == "Y" :
    clear()
    print("PROGRAM HITUNG TOTAL HARGA PRINTER EPSON T20")
    print("--------------------------------------------")   
    hrgPrinter = 660000
    diskon = 0.15   
    a = input("Masukkan Jumlah Printer = ")
    jmlhPrt = int(a)
    totHrg = jmlhPrt * hrgPrinter

    if totHrg > 1500000 :
        totDiskon = diskon * totHrg
        totBy = totHrg - totDiskon
        print()
        print("Diskon 15%")
        print("Total Harga  = Rp.",format(totHrg,',.2f'))
        print("Total Diskon = Rp.",format(totDiskon,',.2f'))
        print("Total Biaya  = Rp.",format(totBy,',.2f')) 
    else :
        totBy = totHrg
        print()
        print("Total Biaya = Rp.",format(totBy,',.2f'))  
    print() 
    jwb = input("Cek Lagi? (y/t) = ")
    if jwb == "t" or jwb == "T" :
        break




    