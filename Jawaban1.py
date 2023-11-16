# Kelas Induk (Superclass)
class Kendaraan:
    def __init__(self, merk, model):
        self.merk = merk
        self.model = model

    def info(self):
        print(f"Kendaraan: {self.merk} {self.model}")

# Kelas Turunan (Subclass)
class Mobil(Kendaraan):
    def __init__(self, merk, model, roda):
        # Memanggil konstruktor kelas induk
        super().__init__(merk, model)
        self.roda = roda

    def info(self):
        print(f"Mobil: {self.merk} {self.model}, Roda: {self.roda}")

# Kelas Turunan Lainnya
class Motor(Kendaraan):
    def __init__(self, merk, model, jenis_mesin):
        # Memanggil konstruktor kelas induk
        super().__init__(merk, model)
        self.jenis_mesin = jenis_mesin

    def info(self):
        print(f"Motor: {self.merk} {self.model}, Mesin: {self.jenis_mesin}")

# Membuat objek dari kelas turunan
mobil = Mobil("Toyota", "Camry", 4)
motor = Motor("Honda", "CBR600RR", "4-tak")

# Memanggil metode info dari masing-masing objek
mobil.info()
motor.info()
