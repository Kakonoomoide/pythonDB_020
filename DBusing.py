import tkinter as tk
from tkinter import messagebox
import sqlite3


# Fungsi untuk hasil prediksi

def prediksi_prodi():
    # Mengambil data dari entry
    nama_siswa = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_Matematika = float(entry_Matematika.get())
    nilai_Kimia = float(entry_Kimia.get())
    nilai_Sejarah = float(entry_Sejarah.get())
    nilai_Ekonomi = float(entry_Ekonomi.get())
    nilai_Geografi = float(entry_Geografi.get())
    nilai_Seni = float(entry_Seni.get())
    nilai_PKN = float(entry_PKN.get())

    # Menentukan hasil prediksi berdasarkan kondisi
    max_nilai = max(nilai_biologi, nilai_fisika, nilai_inggris, nilai_Matematika,
                    nilai_Kimia, nilai_Sejarah, nilai_Ekonomi, nilai_Geografi, nilai_Seni, nilai_PKN)

    if max_nilai == nilai_biologi:
        prediksi = "Kedokteran"
    elif max_nilai == nilai_fisika:
        prediksi = "Teknik"
    elif max_nilai == nilai_inggris:
        prediksi = "Bahasa"
    else:
        prediksi = "Belum dapat diprediksi"

    # Menampilkan hasil prediksi
    hasil_prediksi.config(text=f"Prodi Pilihan: {prediksi}")

    # Menyimpan data ke SQLite
    conn = sqlite3.connect('DataSiswa.db')
    cursor = conn.cursor()

    # Membuat table jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi REAL,
            fisika REAL,
            inggris REAL,
            Matematika REAL,
            Kimia REAL,
            Sejarah REAL,
            Ekonomi REAL,
            Geografi REAL,
            Seni REAL,
            PKN REAL,
            prediksi_fakultas TEXT
        )
    ''')

    # Menyimpan data
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, Matematika, Kimia, Sejarah, Ekonomi, Geografi, Seni, PKN, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, nilai_Matematika, nilai_Kimia, nilai_Sejarah, nilai_Ekonomi, nilai_Geografi, nilai_Seni, nilai_PKN, prediksi))

    # Commit dan tutup koneksi
    conn.commit()
    conn.close()

    # Set nilai kosong pada entry setelah penyimpanan data
    entry_nama.delete(0, 'end')
    entry_biologi.delete(0, 'end')
    entry_fisika.delete(0, 'end')
    entry_inggris.delete(0, 'end')
    entry_Matematika.delete(0, 'end')
    entry_Kimia.delete(0, 'end')
    entry_Sejarah.delete(0, 'end')
    entry_Ekonomi.delete(0, 'end')
    entry_Geografi.delete(0, 'end')
    entry_Seni.delete(0, 'end')
    entry_PKN.delete(0, 'end')

    messagebox.showinfo("Info", "Data berhasil disimpan!")


# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.configure(bg='navy')  # Mengatur latar belakang aplikasi menjadi biru navy

# Membuat label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=(
    "Helvetica", 16), bg='navy', fg='white')
judul_label.grid(row=0, column=0, columnspan=2)

# Membuat entry untuk nama siswa
label_nama = tk.Label(root, text="Nama Siswa:", bg='navy', fg='white')
label_nama.grid(row=1, column=0, sticky='w')
entry_nama = tk.Entry(root)
entry_nama.grid(row=1, column=1)

# Membuat entry untuk nilai Biologi
label_biologi = tk.Label(
    root, text="Nilai Biologi:", bg='navy', fg='white')
label_biologi.grid(row=2, column=0, sticky='w')
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=2, column=1)

# Membuat entry untuk nilai Fisika
label_fisika = tk.Label(
    root, text="Nilai Fisika:", bg='navy', fg='white')
label_fisika.grid(row=3, column=0, sticky='w')
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=3, column=1)

# Membuat entry untuk nilai Inggris
label_inggris = tk.Label(
    root, text="Nilai Inggris:", bg='navy', fg='white')
label_inggris.grid(row=4, column=0, sticky='w')
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=4, column=1)

# Membuat entry untuk nilai Matematika
label_matematika = tk.Label(
    root, text="Nilai Matematika:", bg='navy', fg='white')
label_matematika.grid(row=5, column=0, sticky='w')
entry_Matematika = tk.Entry(root)
entry_Matematika.grid(row=5, column=1)

# Membuat entry untuk nilai Kimia
label_kimia = tk.Label(
    root, text="Nilai Kimia:", bg='navy', fg='white')
label_kimia.grid(row=6, column=0, sticky='w')
entry_Kimia = tk.Entry(root)
entry_Kimia.grid(row=6, column=1)

# Membuat entry untuk nilai Sejarah
label_sejarah = tk.Label(
    root, text="Nilai Sejarah:", bg='navy', fg='white')
label_sejarah.grid(row=7, column=0, sticky='w')
entry_Sejarah = tk.Entry(root)
entry_Sejarah.grid(row=7, column=1)

# Membuat entry untuk nilai Ekonomi
label_ekonomi = tk.Label(
    root, text="Nilai Ekonomi:", bg='navy', fg='white')
label_ekonomi.grid(row=8, column=0, sticky='w')
entry_Ekonomi = tk.Entry(root)
entry_Ekonomi.grid(row=8, column=1)

# Membuat entry untuk nilai Geografi
label_geografi = tk.Label(
    root, text="Nilai Geografi:", bg='navy', fg='white')
label_geografi.grid(row=9, column=0, sticky='w')
entry_Geografi = tk.Entry(root)
entry_Geografi.grid(row=9, column=1)

# Membuat entry untuk nilai Seni
label_seni = tk.Label(
    root, text="Nilai Seni:", bg='navy', fg='white')
label_seni.grid(row=10, column=0, sticky='w')
entry_Seni = tk.Entry(root)
entry_Seni.grid(row=10, column=1)

# Membuat entry untuk nilai PKN
label_pkn = tk.Label(
    root, text="Nilai PKN:", bg='navy', fg='white')
label_pkn.grid(row=11, column=0, sticky='w')
entry_PKN = tk.Entry(root)
entry_PKN.grid(row=11, column=1)

# Membuat button untuk hasil prediksi
prediksi_button = tk.Button(
    root, text="Hasil Prediksi", command=prediksi_prodi, bg='white', fg='navy')
prediksi_button.grid(row=12, column=0, columnspan=2)

# Membuat label untuk hasil prediksi
hasil_prediksi = tk.Label(root, text="", font=(
    "Helvetica", 12), bg='navy', fg='white')
hasil_prediksi.grid(row=13, column=0, columnspan=2)

# Menjalankan GUI
root.mainloop()
