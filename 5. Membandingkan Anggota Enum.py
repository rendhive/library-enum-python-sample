from enum import Enum

class Level(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Level.MEDIUM == Level.HIGH)  # Membandingkan anggota enum
# Fungsi: Menunjukkan perbandingan antara dua anggota enum.
# Kondisi: Ketika Anda ingin mengekspresikan logika diantara anggota enum.