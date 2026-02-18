from enum import Enum
from typing import List

class Flavor(Enum):
    VANILLA = "Vanilla"
    CHOCOLATE = "Chocolate"
    STRAWBERRY = "Strawberry"

def order_ice_cream(flavors: List[Flavor]) -> None:
    for flavor in flavors:
        print(f"Ordering {flavor.value} ice cream.")

order_ice_cream([Flavor.VANILLA, Flavor.STRAWBERRY])
# Fungsi: Menerima list yang berisi pilihan rasa es krim.
# Kondisi: Ketika Anda ingin menyampaikan beberapa pilihan rasa yang ada.