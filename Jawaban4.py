def bagi(angka1, angka2):
    try:
        hasil = angka1 / angka2
        return hasil
    except ZeroDivisionError:
        return "Error: Pembagian oleh nol tidak diizinkan."

# Contoh penggunaan
angka1 = 10
angka2 = 0

hasil_pembagian = bagi(angka1, angka2)
print(f"Hasil pembagian: {hasil_pembagian}")
