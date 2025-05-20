from smartphone import Smartphone

catalog = [
    Smartphone("brand: Xiaomi", "model: Note10", "number: +79857654322"),
    Smartphone("brand: Iphone", "model: ProMax", "number: +79153654324"),
    Smartphone("brand: Samsung", "model: GalaxyUltra", "number: +79267634326"),
    Smartphone("brand: Huawei", "model: PuraPro", "number: +79157324365"),
    Smartphone("brand: Poco", "model: M6", "number: +79067656783")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")