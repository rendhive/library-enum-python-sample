from enum import Enum

class Error(Enum):
    NOT_FOUND = "Error 404: Not Found"
    UNAUTHORIZED = "Error 401: Unauthorized"
    FORBIDDEN = "Error 403: Forbidden"

print(Error.NOT_FOUND.value)
# Fungsi: Mendifinisikan error menggunakan enum untuk meningkatkan keterbacaan.
# Kondisi: Ketika Anda ingin mengelola dan merepresentasikan status kesalahan.