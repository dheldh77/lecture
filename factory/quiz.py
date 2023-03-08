from equipment.duv_equipment import DUVEquipment
from equipment.euv_equipment import EUVEquipment


class SystemA:
    def __init__(self):
        print("System A instance is created")

    def __del__(self):
        print("System A instance is deleted")

    def load(self):
        duv = DUVEquipment()
        duv.load()

    def analyze(self):
        duv = DUVEquipment()
        duv.analyze()

    def report(self):
        duv = DUVEquipment()
        duv.report()


class SystemB:
    def __init__(self):
        print("System B instance is created")

    def __del__(self):
        print("System B instance is deleted")

    def load(self, input: str):
        if input == "duv":
            duv = DUVEquipment()
            duv.load()
        elif input == "euv":
            euv = EUVEquipment()
            euv.load()
        else:
            print("input is invalid")

    def analyze(self, input: str):
        if input == "duv":
            duv = DUVEquipment()
            duv.analyze()
        elif input == "euv":
            euv = EUVEquipment()
            euv.analyze()
        else:
            print("input is invalid")

    def report(self, input: str):
        if input == "duv":
            duv = DUVEquipment()
            duv.reoprt()
        elif input == "euv":
            euv = EUVEquipment()
            euv.report()
        else:
            print("input is invalid")


if __name__ == "__main__":
    system = SystemA()
    system.load()
    system.analyze()
    system.report()