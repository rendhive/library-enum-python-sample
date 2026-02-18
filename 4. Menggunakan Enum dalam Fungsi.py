from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

def move(direction: Direction) -> None:
    print(f"Moving {direction.name}")

move(Direction.NORTH)
# Fungsi: Menggunakan enum sebagai tipe argumen dalam fungsi.
# Kondisi: Ketika Anda ingin membatasi argumen fungsi hanya ke anggota enum tertentu.