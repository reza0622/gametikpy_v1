import socket #libary untuk mengenal device yang digunakan
from time import sleep #libary untuk waktu "sleep" => delay

pc_name = socket.gethostname() #gathostname untuk mengenal nama pc yang digunakan
bentuk_garis = "-"

# Membuat fungsi pesan welcome ketika pertama kali program dijalankan
def pesan_welcome():
    garis = bentuk_garis * (len(pc_name)+8)
    print("\n" + garis)
    print("--- "+pc_name+" ---")
    print( garis + "\n ")

# Membuat pesan exit/keluar
def pesan_exit():
    pesan = "PERMAINAN SELESAI"
    garis = bentuk_garis * (len(pesan)+8)
    
    print("Permainan akan diberhentikan!!!")
    sleep(1)
    print("\n" + garis)
    sleep(1)
    print("--- "+pesan+" ---")
    sleep(1)
    print(garis+"\n\n")
    sleep(1)
    print("Terima Kasih Telah Mencoba Permainan!")

if __name__ == '__main__':
    pesan_welcome()
    pesan_exit()
