# level2.py
import time

def materi_level_2():
    print("""
===================================================================
📖 MATERI LEVEL 2: KULI BANGUNAN OTOMATIS (Looping: For & While)
===================================================================
Looping itu menyuruh komputer melakukan hal yang sama berulang kali 
sampai capek atau sampai targetnya selesai.

1. FOR Loop (Target Pasti):
   "Tolong ketuk pintu ini sebanyak 3 kali." Kamu tahu persis harus 
   berhenti di ketukan ketiga.

2. WHILE Loop (Target Kondisi):
   "Tolong aduk sup ini SAMPAI matang." Kamu tidak tahu berapa kali 
   harus mengaduk, yang penting berhenti kalau sudah matang.
===================================================================
""")

def simulator_level_2():
    print("\n🎮 SIMULATOR LEVEL 2: MESIN PENGETUK PINTU & PEMASAK OTOMATIS")
    
    print("\n--- Uji Coba FOR Loop (Ketuk 3 Kali) ---")
    for i in range(1, 4):
        print(f"🚪 *Tok.. Tok.. Tok..* (Ketukan ke-{i})")
        time.sleep(0.5)
        
    print("\n--- Uji Coba WHILE Loop (Memasak Sup) ---")
    sup_matang = False
    suhu = 30
    
    while not sup_matang:
        print(f"🍲 Sup sedang diaduk... Suhu saat ini: {suhu}°C")
        suhu += 20
        time.sleep(0.5)
        if suhu >= 90:
            sup_matang = True
            
    print("✨ Sup sudah matang sempurna di atas 90°C! Mesin berhenti.")

if __name__ == "__main__":
    materi_level_2()
    simulator_level_2()
