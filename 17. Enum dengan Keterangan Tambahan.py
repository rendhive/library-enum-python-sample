from enum import Enum

class Status(Enum):
    ACTIVE = "Active"  # Status aktif
    INACTIVE = "Inactive"  # Status tidak aktif

print(Status.ACTIVE.name)  # Nama
print(Status.ACTIVE.value)  # Nilai
# Fungsi: Memperlihatkan cara mendefinisikan enum dengan deskripsi tambahan.
# Kondisi: Ketika Anda ingin menambahkan keterangan ke enum untuk dokumentasi lebih baik.