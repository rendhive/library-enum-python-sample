from enum import Enum

class TaskStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

status = TaskStatus.IN_PROGRESS
print(f"Current status: {status.value}")
# Fungsi: Menggunakan enum untuk merepresentasikan status dari suatu tugas.
# Kondisi: Ketika Anda ingin secara jelas mendefinisikan status di dalam aplikasi.