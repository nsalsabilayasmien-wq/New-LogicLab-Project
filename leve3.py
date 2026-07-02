# level3.py

def materi_level_3():
    print("""
===================================================================
📖 LOGICLAB LEVEL 3: KANTONG AJAIB DORAEMON (Functions)
===================================================================
Fungsi (Function) itu seperti tombol ajaib. Sekali kamu buat tombolnya, 
kamu tinggal pencet kapan saja tanpa perlu merakit mesinnya lagi dari awal.

1. Built-in Function (Tombol Bawaan Pabrik):
   Fungsi yang sudah disediakan Python dari sananya. Contoh: print(), 
   input(), len() (untuk menghitung panjang mainan).

2. User Defined Function (Tombol Rakitan Sendiri):
   Tombol yang kamu desain sendiri fungsinya pakai kata kunci 'def'.
===================================================================
""")

def projek_kalkulator_magic():
    print("\n🧙‍♂️ LOGICLAB FINAL PROJECT: MAGIC CALCULATOR 🧙‍♂️")
    print("Kalkulator ini bisa menghitung sekaligus menebak sifat angkamu!")
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        operasi = input("Pilih operasi (+, -, *, /): ")
        
        if operasi == "+":
            hasil = a + b
        elif operasi == "-":
            hasil = a - b
        elif operasi == "*":
            hasil = a * b
        elif operasi == "/":
            hasil = a / b if b != 0 else "Error (Tidak bisa dibagi 0)"
        else:
            print("Operasi tidak dikenali!")
            return

        print(f"🔮 Hasil Mantra: {hasil}")
        if isinstance(hasil, (int, float)):
            if hasil > 100:
                print("🔮 Ramalan: Hasilmu besar sekali! Kamu akan dapat rezeki besar!")
            else:
                print("🔮 Ramalan: Angka yang rendah hati. Kamu orang yang hemat!")
    except ValueError:
        print("❌ Masukkan angka yang valid!")

def projek_sistem_absensi():
    print("\n📝 LOGICLAB FINAL PROJECT: SISTEM ABSENSI SMART 📝")
    daftar_hadir = []
    
    while True:
        nama = input("Masukkan nama mahasiswa (ketik 'selesai' untuk keluar): ").strip()
        if nama.lower() == 'selesai':
            break
        if nama == "":
            print("Nama tidak boleh kosong!")
            continue
        daftar_hadir.append(nama)
        print(f"✅ {nama} berhasil diabsen.")
        
    print("\n=== DAFTAR HADIR KELAS HARI INI ===")
    print(f"Total Mahasiswa Hadir: {len(daftar_hadir)} orang")
    for urutan, mhs in enumerate(daftar_hadir, 1):
        print(f"{urutan}. {mhs}")

def menu_projek_akhir():
    print("\n🎓--- LOGICLAB GRADUASI ---🎓")
    print("Silahkan pilih salah satu projek untuk kamu selesaikan:")
    print("1. Kalkulator Magic")
    print("2. Sistem Absensi Smart")
    
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    if pilihan == "1":
        projek_kalkulator_magic()
    elif pilihan == "2":
        projek_sistem_absensi()
    else:
        print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    materi_level_3()
    menu_projek_akhir()
