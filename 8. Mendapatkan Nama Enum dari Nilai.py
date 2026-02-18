from enum import Enum

class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    CHERRY = 3

print(Fruit(2).name)  # Mendapatkan nama enum dari nilai
# Fungsi: Mendapatkan nama anggota enum berdasarkan nilai.
# Kondisi: Ketika Anda memiliki nilai dan ingin menemukan nama terkait.