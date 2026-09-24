class Vehicle:
    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate
        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def show_info(self):
        print(f"ป้ายทะเบียน: {self.license_plate}")
        print(f"ยี่ห้อ: {self.brand}, รุ่น: {self.model}, ปี: {self.year}")
        print(f"ค่าเช่ารายวัน: {self.daily_rate} บาท")



class Truck(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload

    def show_info(self):
        print("--- ข้อมูลรถบรรทุก (Truck) ---")
        super().show_info()
        print(f"น้ำหนักบรรทุก: {self.payload} ตัน")
