import sqlite3

# Membuat koneksi ke database (file database akan dibuat jika tidak ada)
conn = sqlite3.connect("contoh_database.db")

# Membuat kursor
cursor = conn.cursor()

# Membuat tabel (jika belum ada)
cursor.execute('''CREATE TABLE IF NOT EXISTS mahasiswa 
                  (id INTEGER PRIMARY KEY, nama TEXT, umur INTEGER)''')

# Menambahkan data ke dalam tabel
cursor.execute("INSERT INTO mahasiswa (nama, umur) VALUES (?, ?)", ("Suyanto", 20))
cursor.execute("INSERT INTO mahasiswa (nama, umur) VALUES (?, ?)", ("Rafi Ananda", 21))

# Melakukan query untuk mendapatkan data
cursor.execute("SELECT * FROM mahasiswa")
data_mahasiswa = cursor.fetchall()

# Menampilkan data
print("Data Mahasiswa:")
for row in data_mahasiswa:
    print(f"ID: {row[0]}, Nama: {row[1]}, Umur: {row[2]}")

# Menutup kursor dan koneksi
cursor.close()
conn.commit()
conn.close()
