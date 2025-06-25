import mysql.connector # Import the MySQL connector library

# membuat variabel untuk koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",  # Database host,
    user="root", # Database user
    password="",  # Database password
    database="mini_market"  # Database name
)

#Membuat funtion menambah barang (insert)
def tambah_barang(kode_barang, nama_barang, stok_barang):
    cursor = db.cursor()  # Create a cursor object to execute SQL queries
    sql = "INSERT INTO tbl_barang (kode_barang, nama_barang, stok_barang) VALUES (%s, %s, %s)" #insert sesuai dengan nama tabel barang
    values = (kode_barang, nama_barang, stok_barang)
    cursor.execute(sql, values)  # Execute the SQL query with the provided values
    db.commit()  # Commit the transaction to save changes
    if cursor.rowcount > 0:
        print(f"Barang {nama_barang} berhasil ditambahkan.") # Print success message
    else:
        print(f"Gagal menambahkan barang {nama_barang}.") # Print failure message
    
    # print(f"Barang {nama_barang} berhasil ditambahkan.")
    

# print(db.is_connected())  # Check if the connection is successful