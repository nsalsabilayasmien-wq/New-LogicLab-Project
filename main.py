# main.py
import sys
# Import modular dari file lain
import level1
import level2
import level3

def main_menu():
    while True:
        print("\n" + "="*50)
        print("🚀 PROGRAM LES KODING MAHASISWA SEMESTER 1 🚀")
        print("          Approach: Python for 5 Years Old")
        print("="*50)
        print("1. [Level 1] Algoritma, Flowchart, If-Else, & Array")
        print("2. [Level 2] Looping (For & While)")
        print("3. [Level 3] Functions & Projek Akhir")
        print("4. Keluar dari Program")
        print("="*50)
        
        pilihan = input("Pilih Level Belajarmu (1-4): ").strip()
        
        if pilihan == "1":
            level1.materi_level_1()
            input("\nTekan Enter untuk lanjut ke Simulator...")
            level1.simulator_level_1()
        elif pilihan == "2":
            level2.materi_level_2()
            input("\nTekan Enter untuk lanjut ke Simulator...")
            level2.simulator_level_2()
        elif pilihan == "3":
            level3.materi_level_3()
            input("\nTekan Enter untuk lanjut ke Tantangan Projek Akhir...")
            level3.menu_projek_akhir()
        elif pilihan == "4":
            print("\n👋 Terima kasih sudah belajar! Sampai jumpa di kelas koding berikutnya!")
            sys.exit()
        else:
            print("❌ Pilihan tidak valid. Masukkan angka 1 sampai 4.")
            
        input("\nTekan Enter untuk kembali ke Menu Utama...")

if __name__ == "__main__":
    main_menu()
