from enum import Enum

class Vehicle(Enum):
    CAR = "Car"
    BIKE = "Bike"
    TRUCK = "Truck"

# Menambahkan anggota enum secara dinamis (tidak disarankan biasanya)
Vehicle.BUS = "Bus"
print(Vehicle.BUS.value)
# Fungsi: Demonstrasi penambahan anggota ke enum, meskipun bukan praktik umum.
# Kondisi: Menunjukkan bahwa Enum bisa diperluas dengan cara tertentu.