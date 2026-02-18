from enum import Enum

class State(Enum):
    INITIAL = 0
    LOADING = 1
    LOADED = 2
    ERROR = 3

def load_data(state: State) -> None:
    if state == State.LOADING:
        print("Loading data...")
    elif state == State.LOADED:
        print("Data loaded successfully!")
    elif state == State.ERROR:
        print("Error loading data.")

load_data(State.LOADING)
# Fungsi: Menerima enum untuk mendemonstrasikan alur status dalam program.
# Kondisi: Ketika Anda berurusan dengan transisi status dalam aplikasi.