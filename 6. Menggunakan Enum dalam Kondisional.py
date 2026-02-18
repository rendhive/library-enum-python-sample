from enum import Enum

class TrafficLight(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3

def action_based_on_light(light: TrafficLight) -> None:
    if light == TrafficLight.RED:
        print("Stop!")
    elif light == TrafficLight.GREEN:
        print("Go!")
    else:
        print("Caution!")

action_based_on_light(TrafficLight.GREEN)
# Fungsi: Eksplorasi logika berdasarkan nilai enum dalam kondisi.
# Kondisi: Ketika Anda perlu mengambil tindakan berdasarkan keadaan yang terdefinisi.