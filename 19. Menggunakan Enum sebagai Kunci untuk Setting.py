from enum import Enum

class Settings(Enum):
    VOLUME = "Volume"
    BRIGHTNESS = "Brightness"
    CONTRAST = "Contrast"

def update_setting(setting: Settings, value: int) -> None:
    print(f"Updating {setting.value} to {value}")

update_setting(Settings.VOLUME, 75)
# Fungsi: Menggunakan enum sebagai kunci untuk pengaturan.
# Kondisi: Ketika Anda ingin menerapkan pengaturan aplikasi yang terstandardisasi.