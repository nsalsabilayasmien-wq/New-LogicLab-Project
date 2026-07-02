# level1.py

def materi_level_1():
    print("""
===================================================================
📖 MATERI LEVEL 1: PETA HARTA KARUN (Algoritma, Flowchart, If-Else, List)
===================================================================
1. Algoritma & Flowchart: 
   Bayangkan kamu mau bikin susu cokelat. Langkahnya: ambil gelas -> 
   tuang susu -> aduk. Nah, urutan langkah itu namanya ALGORITMA. 
   Kalau gambar langkah-langkah itu pakai kotak dan panah, itu FLOWCHART.

2. If-Else (Sebab-Akibat):
   "JIKA hujan, MAKA bawa payung. KALAU TIDAK hujan, tidak bawa."
   Di coding, ini dipakai buat gerbang keputusan.

3. Array / List (Kotak Mainan):
   Kamu punya kotak besar untuk menyimpan semua mainan mobil-mobilanmu. 
   Daripada bikin 10 kotak kecil, mending 1 kotak besar disekat-sekat.
===================================================================
""")

def simulator_level_1():
    print("\n🎮 SIMULATOR LEVEL 1: ROBOT PENJAGA GERBANG")
    print("Mari masukkan mainan ke dalam kotak (Array/List) untuk robot!")
    
    # Inisialisasi List/Array
    kotak_mainan = ["robot", "mobil", "lego"]
    print(f"Isi kotak saat ini: {kotak_mainan}")
    
    # Input dari user
    mainan_baru = input("Masukkan nama mainan baru untuk robot: ").strip().lower()
    kotak_mainan.append(mainan_baru)
    print(f"Isi kotak sekarang: {kotak_mainan}")
    
    # Logika If-Else
    print("\n--- Robot memeriksa isi kotak ---")
    if "monster" in kotak_mainan:
        print("🤖 Robot: 'BAHAYA! Ada monster di dalam kotak! Akses Ditolak!'")
    else:
        print("🤖 Robot: 'Aman. Semua mainan baik. Akses Diterima!'")

if __name__ == "__main__":
    materi_level_1()
    simulator_level_1()
