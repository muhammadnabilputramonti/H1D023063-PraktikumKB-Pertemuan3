1. Import Library

import random
import datetime
random digunakan untuk menghasilkan nomor pesanan secara acak.
datetime digunakan untuk mencetak waktu pemesanan.

2. Struktur Data Menu
menu = {
    "1": {"nama": "Nasi Goreng", "harga": 25000},
    "2": {"nama": "Mie Ayam", "harga": 20000},
    "3": {"nama": "Ayam Geprek", "harga": 22000},
    "4": {"nama": "Es Teh", "harga": 5000}
}

Menu makanan disimpan dalam bentuk dictionary, dengan nomor sebagai kunci (key) dan nilai berupa sub-dictionary berisi nama dan harga makanan.


3. Fungsi tampilkan_menu()
def tampilkan_menu():
    print("\n=== MENU MAKANAN ===")
    for key, item in menu.items():
        print(f"{key}. {item['nama']} - Rp{item['harga']}")

Fungsi ini mencetak daftar menu makanan dengan nomor, nama, dan harga makanan.

4. Fungsi buat_pesanan()
def buat_pesanan(pilihan_preset=None):
    pesanan = []
    total_harga = 0
    index = 0
    
    while True:
        tampilkan_menu()
        if pilihan_preset:
            if index < len(pilihan_preset):
                pilihan = pilihan_preset[index]
                index += 1
            else:
                pilihan = 'selesai'
        else:
            pilihan = input("Masukkan nomor menu (atau ketik 'selesai' untuk mengakhiri): ")
        
        if pilihan.lower() == 'selesai':
            break
        
        if pilihan in menu:
            pesanan.append(menu[pilihan]["nama"])
            total_harga += menu[pilihan]["harga"]
            print(f"{menu[pilihan]['nama']} ditambahkan ke pesanan.\n")
        else:
            print("Nomor menu tidak valid!\n")
    
    return pesanan, total_harga

Fungsi ini memungkinkan pengguna untuk memilih makanan berdasarkan nomor menu.
Variabel pesanan: Menyimpan daftar makanan yang dipesan.
Variabel total_harga: Menyimpan total harga pesanan.
Jika pengguna memasukkan nomor menu yang valid, makanan akan ditambahkan ke pesanan dan harga ditotal.
Jika pengguna mengetik "selesai", proses pemesanan berhenti.

Catatan:
pilihan_preset adalah parameter opsional untuk memberikan input tanpa perlu interaksi langsung (berguna untuk pengujian).

5. Fungsi cetak_struk()
def cetak_struk(pesanan, total):
    if not pesanan:
        print("\nTidak ada pesanan yang dibuat.")
        return
    
    print("\n=== STRUK PEMBELIAN ===")
    for item in pesanan:
        print(f"- {item}")
    print(f"Total Harga: Rp{total}")
    print(f"Nomor Pesanan: {random.randint(1000, 9999)}")
    print(f"Waktu Pemesanan: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

Fungsi ini mencetak struk pesanan, yang berisi:
Daftar makanan yang dipesan.
Total harga pesanan.
Nomor pesanan (dibuat secara acak).
Waktu pemesanan (menggunakan `datetime`).


6. Fungsi main()
def main():
    while True:
        pesanan, total = buat_pesanan()
        cetak_struk(pesanan, total)
        ulang = input("\nApakah Anda ingin memesan lagi? (ya/tidak): ")
        if ulang.lower() != 'ya':
            print("Terima kasih telah memesan!")
            break

Fungsi ini mengatur alur utama program, yaitu:
  1. Memanggil buat_pesanan() untuk menerima pesanan.
  2. Memanggil cetak_struk() untuk mencetak struk pemesanan.
  3. Menanyakan apakah pengguna ingin memesan lagi.
  4. Jika pengguna menjawab "tidak", program menampilkan pesan terima kasih dan berhenti.

---

7. Menjalankan Program
main()

Memanggil fungsi main() untuk memulai program.
