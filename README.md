# 📝 To-Do List App (Python + TXT File Storage)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

---

## 📝 Deskripsi Proyek
Aplikasi **To-Do List** ini dibuat menggunakan **Python** dengan penyimpanan berbasis **file `.txt`**, sehingga setiap tugas yang ditambahkan atau dihapus akan tersimpan secara permanen meskipun program ditutup.  

Fokus proyek ini adalah untuk melatih pemahaman dasar pemrograman Python, seperti:
- **Manipulasi file** (membaca, menulis, menimpa data)
- **List comprehension** untuk memfilter data
- **Penggunaan fungsi** untuk modularisasi kode
- **Error handling** untuk mencegah crash
- **Pemrosesan string** menggunakan `.strip()` dan `.startswith()`

Program ini juga dilengkapi dengan **fitur log aktivitas** yang mencatat setiap penambahan atau penghapusan tugas beserta **tanggal dan waktunya**, sehingga pengguna dapat melihat riwayat penggunaan aplikasi.

Aplikasi ini dirancang **sederhana, ringan, dan tanpa dependensi tambahan**, sehingga bisa langsung dijalankan di semua perangkat yang memiliki Python 3.x.

---

## ✨ Fitur Utama
- **Tambah Tugas** → Simpan tugas baru ke `to-do.txt`
- **Lihat Tugas** → Menampilkan semua tugas aktif
- **Hapus Tugas** → Pilih berdasarkan nomor urut
- **Log Aktivitas** → Mencatat setiap penambahan & penghapusan tugas dengan tanggal & waktu
- **File Storage** → Data tersimpan di `to-do.txt` sehingga tetap ada walaupun program ditutup

---

## 📂 Struktur File
📁 todo-list/
│── to-do.py # Script utama
│── to-do.txt # Penyimpanan daftar tugas & log
└── README.md # Dokumentasi proyek

---

## 💻 Cara Menjalankan

### 1️⃣ Persiapan
Pastikan **Python** sudah terinstall di komputer.  
Cek versi Python:
```bash
python --version
git clone https://github.com/username/todo-list.git
cd todo-list
python to-do.py
=== To-Do List ===
1. Belajar Python
2. Baca buku
[2025-08-09 15:45:10] Tugas ditambahkan: Belajar Python
[2025-08-09 15:50:12] Melihat daftar tugas
⚙️ Alur Program
Baca file to-do.txt jika sudah ada, atau buat file baru jika belum ada.

Pisahkan data tugas & log (log selalu diawali dengan [).

Tampilkan menu:

Tambah tugas

Lihat daftar tugas

Hapus tugas

Keluar program

Simpan perubahan ke to-do.txt setiap ada aksi.

Catat log saat menambah/menghapus tugas.

🎥 Demo Program

🛠 Teknologi yang Digunakan
Python 3.x

File Storage menggunakan format .txt
