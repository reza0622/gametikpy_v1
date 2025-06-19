import random
from lib import pesan_welcome

#membuat funtion mulai untuk permainan

def mulai():
    # Loop untuk mengulang permainan
    while True:
        bentuk_lubang = "|___|" #bentuk lubang tikus
        lubang_kosong = [bentuk_lubang] * 4 #Jumlah lubang tikus yang kosong
        lubang = lubang_kosong.copy() #tempat/lubang keberadaaan Tikus
        tikus = random.randint(1, 4) #variabel keberadaan tikus secara rundom
        lubang [tikus - 1] = "|>!<|" #bentuk keberadaan tikus, tanda [] => list/array yang diawali dengan index 0. maka [tikus - 1] => angka random di tikus di kurang 1, karena perhitungan manusia diawali dengan 1 sedangkan perhitungan dalam array/list/pemrograman diawali dengan 0

        # mengubah nilai array/list/menghilangkan "[,]" menjadi string dengan fungsi ".join"
        lubang_kosong = ' '.join(lubang_kosong) #mengubah tampilan/array lubang kosong menjadi rapih tanpa "[]", tanda (' '.join") spasi kosong dapat diisi dengan apa saja untuk mengganti list/array
        lubang = ' '.join(lubang) #mengubah nilai/list/array lunang
        
        print(f"Perhatikan lubang tikus dibawah ini:\n\n{lubang_kosong}\n\n") #kutip/tanda petik 3 ('''....''') agar bisa menambah baris baru atau membaca baris baru

            # membuat inputan variabel/pilahan user dan variabel konfirmasi
        pilihan_user = int(input("Menurut kamu, ada di lubang mana tikus berada [1/2/3/4]: "))
        while pilihan_user > 4: #tidak jalan jika inputan kosong dan 0/kurang dari 1
            pilihan_user = int(input("\nPiliahan yang kamu masukan TIDAK ada\nMasukan angka (1/2/3/4): "))
        # konfirmasi_user = input("\nApakah kamu Yakin? [y/n] : ")
            #membuat kondisi konfirmasi jawaban
        # if konfirmasi_user == "n":
                # print("\nPermaianan dihentikan!, Terimakasih telah mencoba.")
                # exit() #funtion exit untuk mengakhiri program
        # elif konfirmasi_user == "y":
        if pilihan_user == tikus:
            print("\n " + lubang + "\n\nYeah!!! Pilihan mu benar, Tikus berada di lubang nomor " + str(pilihan_user) + "\n") # tanda "\n" untuk mendorong ke garis barus atau Enter
        else:
            print(f"\n{lubang}\n\nSayang Sekali Pilihanmu Salah, Tikus Berada dinomor {tikus}")
        # else:
        #     print("Jawaban yang kamu masukan salah. Permainan dihentikan!")
        #     exit()
        
        # membuat inputan untuk pertanyaan apakah permainan dilanjutkan atau tidak
        main_lagi = input("\n\nApakah ingin bermain kembali (y/n): ")
        if main_lagi == 'n':
            break #fungsi "break" untuk menyelesaikan while atau looping

if __name__ == '__main__':
    mulai()