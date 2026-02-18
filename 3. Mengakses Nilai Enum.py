from enum import Enum

class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2

print(Status.ACTIVE.value)  # Mengakses nilai dari enum
# Fungsi: Mengakses nilai yang menyertainya dari anggota enum.
# Kondisi: Ketika Anda perlu menggunakan nilai numerik dari enum.