import random #libary Random dari python
from lib import pesan_welcome, pesan_exit
from games import tikpy
from tools import warung

#membuat fungsi menu
def menu():
    user_menu = int(input('Menu Pilih Permainan:\n 1. Tikpy\n 2. tools\n\nMasukan Pilihan Kamu: '))
    if user_menu == 1:
        tikpy.mulai()
    elif user_menu == 2:
        warung.mulai_tools
    else:
        user_menu = int(input('\n\nMaaf pilihan kamu kosong/tidak ada,\n\nMohon masukan kembali pilihanmu: '))
        menu()
#membuat fungsi main
def main():
    pesan_welcome()
    menu()
    pesan_exit()

#untuk mengurutkan/menjalankan fungsi mana dulu yang dieksekusi (if __name__ == '__main__')
if __name__ == '__main__':
    main() # => panggil fungsi yang ingin di eksekusi
    




# Code => Coretan & Catatan!!!

#variabel judul permainan
# pembuka = "Permainan Tebak Tikus"

# print("----------------------------------------")
# print(f"------ {pembuka} -----------") #"f" untuk format/agar bisa memasukan/memanggil variabel "{...}"
# print("----------------------------------------")

# memanggil fungsi lib
# pesan_welcome("SELAMAT DATANG DIPERMAINAN")

# membuat nama user dan pertanyaan
# nama_user = input("Siapa nama kamu : ")
#jika user tidak memasukan nama maka akan mengulang/looping
# while nama_user == "": #while salah satu fungsi loop-in selain for. perbedaan while dengang for?
#     nama_user = input("Coba masukan nama kamu dahulu: ")

# pesan_welcome("Hallo "+nama_user+" !!!")
# print("Hallo " + nama_user + "!")

