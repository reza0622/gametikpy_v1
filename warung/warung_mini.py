import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adjust the path to include the parent directory

import main 
from services import db # Importing the database service module

#Membuat fungsi menu untuk menambah barang
def add():
    # buat variabel untuk inputan user sersuai dengan tabel database
    kode_barang = input("Masukan Kode Barang: ")
    nama_barang = input("Masukan Nama Barang: ")
    stok_barang = int(input("Masukan Stok Barang: "))
    
    db.tambah_barang(kode_barang, nama_barang, stok_barang) # Call the function to add the item to the database

# Membuat fungsi untuk mengecek barang
def cek_barang():
    pass

def mulai_tools():
    while True:
        menu =int(input('\nSelamat Datang Di Warung Tikpy!\n\nPilih Menu:\n 1. Tambah Barang\n 2. Cek Barang\n 3. Kembali \n\nMasukan Pilihan Kamu: '))
        if menu == 1:
            add()
        elif menu == 2:
            cek_barang()
        elif menu == 3:
            main.menu()
        else:
            break
            
            
    
if __name__ == '__main__': # => program ini biasakan ada untuk membuat module
    mulai_tools()