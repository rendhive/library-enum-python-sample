from enum import Enum

class MenuOption(Enum):
    START = "Start Game"
    LOAD = "Load Game"
    EXIT = "Exit"

print(f"Menu:\n1. {MenuOption.START.value}\n2. {MenuOption.LOAD.value}\n3. {MenuOption.EXIT.value}")
# Fungsi: Menggunakan enum untuk menyusun pilihan menu.
# Kondisi: Ketika Anda ingin membuat menu interaktif di aplikasi Anda.