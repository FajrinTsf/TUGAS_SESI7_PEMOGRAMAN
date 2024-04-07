def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area


def calculate_rectangle_area(length, width):
    area = length * width
    return area


def is_odd_or_even(number):
    if number % 2 == 0:
        result = "GENAP"
    else:
        result = "GANJIL"
    return result


def main():
    print("__________________Rumus Calculator __________________")
    print("1. Hitung luas segitiga")
    print("2. Hitung luas persegi panjang")
    print("3. Menentukan angka ganjil dan genap")
    print("4. Quit")

    while True:
        try:
            choice = int(
                input("======Masukkan pilihan Anda (1/2/3/4):======="))
            if choice == 1:
                base = float(input("Masukkan panjang alas segitiga: "))
                height = float(input("Masukkan tinggi segitiga: "))
                area = calculate_triangle_area(base, height)
                print(f"Luas segitiga adalah: {area}")
            elif choice == 2:
                length = float(input("Masukkan panjang persegi panjang: "))
                width = float(input("Masukkan lebar  persegi panjang: "))
                area = calculate_rectangle_area(length, width)
                print(f"Luas persegi panjang adalah: {area}")
            elif choice == 3:
                number = int(input("Masukkan angka: "))
                result = is_odd_or_even(number)
                print(f"Angka {number} adalah {result}")
            elif choice == 4:
                print("======Terima kasih telah menggunakan Rumus Calculator!======")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")


if __name__ == "__main__":
    main()
