from equipment.equipment import Equipment


class DUVEquipment(Equipment):
    def __init__(self):
        print("duv instance is created")

    def __del__(self):
        print("duv instance is created")

    def load(self):
        print("load_duv_data")

    def analyze(self):
        print("analyze duv")

    def report(self):
        print("report duv productivty")