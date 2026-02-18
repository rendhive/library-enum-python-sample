from enum import Enum

class Action(Enum):
    START = "Start"
    STOP = "Stop"
    PAUSE = "Pause"

def perform_action(action: Action) -> None:
    print(f"Action performed: {action.value}")

perform_action(Action.START)
# Fungsi: Menerima enum sebagai argumen untuk menentukan tindakan yang dilakukan.
# Kondisi: Ketika Anda ingin menjalankan logika berdasarkan aksi yang terdefinisi.