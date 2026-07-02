# main.py
import sys
import level1
import level2
import level3

def main_menu():
    while True:
        print("\n" + "="*50)
        print("🔬 WELCOME TO LOGICLAB 🔬")
        print("   Python Learning Environment for Semester 1")
        print("="*50)
        print("1. [Level 1] Algoritma, Flowchart, If-Else, & Array")
        print("2. [Level 2] Looping (For & While)")
        print("3. [Level 3] Functions & Projek Akhir")
        print("4. Keluar dari LogicLab")
        print("="*50)
        
        pilihan = input("Pilih Level Belajarmu (1-4): ").strip()
        
        if pilihan == "1":
            level1.materi_level_1()
            input("\nTekan Enter untuk masuk ke Simulator...")
            level1.simulator_level_1()
        elif pilihan == "2":
            level2.materi_level_2()
            input("\nTekan Enter untuk masuk ke Simulator...")
            level2.simulator_level_2()
        elif pilihan == "3":
            level3.materi_level_3()
            input("\nTekan Enter untuk masuk ke Tantangan Projek Akhir...")
            level3.menu_projek_akhir()
        elif pilihan == "4":
            print("\n👋 Terima kasih telah belajar di LogicLab! Pintu lab ditutup.")
            sys.exit()
        else:
            print("❌ Pilihan tidak valid. Masukkan angka 1 sampai 4.")
            
        input("\nTekan Enter untuk kembali ke Menu Utama...")

if __name__ == "__main__":
    main_menu()
