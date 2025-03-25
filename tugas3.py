import random
import datetime

# Struktur Data: Menu dalam bentuk dictionary
menu = {
    "1": {"nama": "Nasi Goreng", "harga": 25000},
    "2": {"nama": "Mie Ayam", "harga": 20000},
    "3": {"nama": "Ayam Geprek", "harga": 22000},
    "4": {"nama": "Es Teh", "harga": 5000}
}

# Menampilkan menu makanan
def tampilkan_menu():
    print("\n=== MENU MAKANAN ===")
    for key, item in menu.items():
        print(f"{key}. {item['nama']} - Rp{item['harga']}")

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

def main():
    while True:
        pesanan, total = buat_pesanan()
        cetak_struk(pesanan, total)
        ulang = input("\nApakah Anda ingin memesan lagi? (ya/tidak): ")
        if ulang.lower() != 'ya':
            print("Terima kasih telah memesan!")
            break

# Jalankan program
main()
