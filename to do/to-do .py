import datetime

def tulis_log(pesan):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("to-do.txt", "a") as file:
        file.write(f"[{waktu}] {pesan}\n")

def tambah_tugas():
    tugas = input("Masukkan tugas baru: ")
    with open("to-do.txt", "a") as file:
        file.write(tugas + "\n")  # Simpan tugas mentah
    tulis_log(f"Tugas ditambahkan: {tugas}")
    print("Tugas berhasil ditambahkan!")

def lihat_tugas():
    try:
        with open("to-do.txt", "r") as file:
            daftar = file.readlines()
            daftar = [t.strip() for t in daftar if not t.startswith("[")]# Hanya tugas mentah
            if daftar:
                print("\nDaftar Tugas:")
                for i, t in enumerate(daftar, start=1):
                    print(f"{i}. {t}")
            else:
                print("Tidak ada tugas.")
        tulis_log("Melihat daftar tugas")
    except FileNotFoundError:
        print("Belum ada daftar tugas.")
def hapus_tugas():
    lihat_tugas()
    try:
        with open("to-do.txt", "r") as file:
            semua_baris = file.readlines()

        # Pisahkan log & tugas mentah
        daftar_tugas = [t for t in semua_baris if not t.startswith("[")]
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))

        if 1 <= nomor <= len(daftar_tugas):
            tugas_dihapus = daftar_tugas[nomor - 1].strip()
            daftar_tugas.pop(nomor - 1)

            # Gabungkan kembali log lama + daftar tugas baru
            semua_log = [t for t in semua_baris if t.startswith("[")]
            with open("to-do.txt", "w") as file:
                file.writelines(daftar_tugas + semua_log)

            tulis_log(f"Tugas dihapus: {tugas_dihapus}")
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tugas tidak valid.")
    except (ValueError, FileNotFoundError):
        print("Terjadi kesalahan!")

# Menu utama
while True:
    print("\n===== TO-DO LIST =====")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        lihat_tugas()
    elif pilihan == "2":
        tambah_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        tulis_log("Keluar dari program")
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid!")
