import sys # Importing sys to manipulate the Python path
import os # Importing os to work with file paths

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Adjust the path to include the parent directory

import main 
from services import db # Importing the database service module

#Membuat fungsi menu untuk menambah barang
def add():
    # buat variabel untuk inputan user sersuai dengan tabel database
    kode_barang = input("\nMasukan Kode Barang: ")
    nama_barang = input("\nMasukan Nama Barang: ")
    harga_barang = int(input("\nMasukan Harga Barang: "))
    stok_barang = int(input("\nMasukan Stok Barang: "))
    
    db.tambah_barang(kode_barang, nama_barang, harga_barang, stok_barang) # Call the function to add the item to the database

# Membuat fungsi untuk mengecek barang
def check():
    items = db.cek_barang()  # Call the function to fetch all items from the database
    for item in items: # Loop through each item in the fetched items
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'\nPersedian Barang:\n\nKode Barang: {kode_barang}\nNama Barang: {nama_barang}\nHarga Barang: Rp {harga_barang}\nStok Barang: {stok_barang}\n') # Print the details of the items

def mulai_tools():
    while True:
        menu =int(input('\nSelamat Datang Di Warung Tikpy!\n\nPilih Menu:\n 1. Tambah Barang\n 2. Cek Barang\n 3. Kembali \n\nMasukan Pilihan Kamu: '))
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break
            
            
    
if __name__ == '__main__': # => program ini biasakan ada untuk membuat module
    mulai_tools()