class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama  # Atribut pribadi
        self.__nim = nim    # Atribut pribadi
        self.__jurusan = jurusan  # Atribut pribadi

    # Metode untuk mendapatkan nilai atribut pribadi
    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def get_jurusan(self):
        return self.__jurusan

    # Metode untuk mengubah nilai atribut pribadi
    def set_nama(self, nama):
        self.__nama = nama

    def set_nim(self, nim):
        self.__nim = nim

    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan

    def info(self):
        print(f"Nama: {self.__nama}, NIM: {self.__nim}, Jurusan: {self.__jurusan}")

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("Suyanto", "20220801301", "Teknik Informatika")

# Mengakses dan mengubah nilai atribut melalui metode
print("Nama awal:", mahasiswa1.get_nama())
mahasiswa1.set_nama("Suyanto")
print("Nama setelah diubah:", mahasiswa1.get_nama())

# Menggunakan metode info
mahasiswa1.info()
