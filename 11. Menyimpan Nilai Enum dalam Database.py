from enum import Enum

class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"

# Simulasi penyimpanan
vehicle = VehicleType.CAR
print(f"Saving vehicle type: {vehicle.value}")
# Fungsi: Menyimpan nilai enum ke dalam database atau struktur data lain.
# Kondisi: Ketika Anda ingin menyimpan data terstandardisasi.