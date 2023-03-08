from equipment.equipment import Equipment


class EUVEquipment(Equipment):
    def __init__(self):
        print("euv instance is created")

    def __del__(self):
        print("euv instance is created")

    def load(self):
        print("load_euv_data")

    def analyze(self):
        print("analyze euv")

    def reoprt(self):
        print("report euv productivty")