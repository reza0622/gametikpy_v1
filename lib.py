# Membuat fungsi pesan welcome ketika pertama kali program dijalankan
def pesan_welcome(title):
    bentuk_garis = "-" * (len(title)+8)
    print("\n" + bentuk_garis)
    print("--- "+title+" ---")
    print(bentuk_garis + "\n ")

# pesan_welcome('hallo')