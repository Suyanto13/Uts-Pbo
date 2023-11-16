class NadaDering:
    def bersuara(self):
        pass

class Android(NadaDering):
    def bersuara(self):
        return "Kring Kring!"

class Iphone(NadaDering):
    def bersuara(self):
        return "Tut Tut!"

# Fungsi yang menggunakan polymorphism
def main():
    Dering_hp = [Android(), Iphone()]

    for NadaDering in Dering_hp:
        print(NadaDering.bersuara())

if __name__ == "__main__":
    main()
