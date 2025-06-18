import random #libary Random dari python
from lib import pesan_welcome

#variabel judul permainan
# pembuka = "Permainan Tebak Tikus"
tikus = random.randint(1, 4) #variabel keberadaan tikus secara rundom
bentuk_lubang = "|___|" #bentuk lubang tikus
lubang_kosong = [bentuk_lubang] * 4 #Jumlah lubang tikus yang kosong
lubang = lubang_kosong.copy() #tempat/lubang keberadaaan Tikus
lubang [tikus - 1] = "|>!<|" #bentuk keberadaan tikus, tanda [] => list/array yang diawali dengan index 0. maka [tikus - 1] => angka random di tikus di kurang 1, karena perhitungan manusia diawali dengan 1 sedangkan perhitungan dalam array/list/pemrograman diawali dengan 0

# mengubah nilai array/list/menghilangkan "[,]" menjadi string dengan fungsi ".join"
lubang_kosong = ' '.join(lubang_kosong) #mengubah tampilan/array lubang kosong menjadi rapih tanpa "[]", tanda (' '.join") spasi kosong dapat diisi dengan apa saja untuk mengganti list/array
lubang = ' '.join(lubang) #mengubah nilai/list/array lunang

# print("----------------------------------------")
# print(f"------ {pembuka} -----------") #"f" untuk format/agar bisa memasukan/memanggil variabel "{...}"
# print("----------------------------------------")

# memanggil fungsi lib
pesan_welcome("SELAMAT DATANG DIPERMAINAN")

# membuat nama user dan pertanyaan
nama_user = input("Siapa nama kamu : ")
#jika user tidak memasukan nama maka akan mengulang/looping
while nama_user == "": #while salah satu fungsi loop-in selain for. perbedaan while dengang for?
    nama_user = input("Coba masukan nama kamu dahulu: ")

pesan_welcome("Hallo "+nama_user+" !!!")
# print("Hallo " + nama_user + "!")

# Loop untuk mengulang permainan
while True:
    print(f'''Perhatikan lubang tikus dibawah ini:

    {lubang_kosong}
    ''') #kutip/tanda petik 3 ('''....''') agar bisa menambah baris baru atau membaca baris baru

        # membuat inputan variabel/pilahan user dan variabel konfirmasi
    pilihan_user = int(input("Menurut kamu, ada di lubang mana tikus berada [1/2/3/4]: "))
    while pilihan_user > 4: #tidak jalan jika inputan kosong dan 0/kurang dari 1
        pilihan_user = int(input("Piliahan yang kamu masukan TIDAK ada \nMasukan angka (1/2/3/4): "))
    konfirmasi_user = input("\nApakah kamu Yakin? [y/n] : ")
        #membuat kondisi konfirmasi jawaban
    if konfirmasi_user == "n":
            print("\nPermaianan dihentikan!, Terimakasih telah mencoba.")
            exit() #funtion exit untuk mengakhiri program
    elif konfirmasi_user == "y":
        if pilihan_user == tikus:
            print("\n " + lubang + "\n\nYeah!!! Pilihan mu benar, Tikus berada di lubang nomor " + str(pilihan_user) + "\n") # tanda "\n" untuk mendorong ke garis barus atau Enter
        else:
            print(f"\n {lubang} \n\nSayang Sekali Pilihanmu Salah, Tikus Berada dinomor {tikus} \n ")
    else:
        print("Jawaban yang kamu masukan salah. Permainan dihentikan!")
        exit()
    
    # membuat inputan untuk pertanyaan apakah permainan dilanjutkan atau tidak
    main_lagi = input("\n\n Apakah ingin bermain kembali (y/n): ")
    if main_lagi == 'n':
        break #fungsi "break" untuk menyelesaikan while atau looping
pesan_welcome("PERMAINAN SELESAI !!!")
