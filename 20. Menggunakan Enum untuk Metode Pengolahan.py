from enum import Enum

class ProcessMethod(Enum):
    ADDITION = "Addition"
    SUBTRACTION = "Subtraction"

def calculate(method: ProcessMethod, a: int, b: int) -> int:
    if method == ProcessMethod.ADDITION:
        return a + b
    elif method == ProcessMethod.SUBTRACTION:
        return a - b
    return 0

print(calculate(ProcessMethod.ADDITION, 5, 3))  # 8
print(calculate(ProcessMethod.SUBTRACTION, 5, 3))  # 2
# Fungsi: Menggunakan enum untuk menentukan metode perhitungan tertentu.
# Kondisi: Ketika Anda ingin melakukan operasi berbeda berdasarkan pilihan enum.