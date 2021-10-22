#APLIKASI INPUTAN DATA MAHASISWA

import os
import sys

class mahasiswa:
        nama=""
        nim=""
pilih = 0
dataSiswa = []

def Menu () :
        os.system ('cls')
        print("Menu Aplikasi Data Siswa")
        print("-------------------------------------------")
        print("1.Input Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Update Data Siswa")
        print("4. Hapus Data Siswa")
        print("5. Author")
        print("6. Keluar Aplikasi")
        pilih = int(input("Masukkan Pilihan Anda :"))
