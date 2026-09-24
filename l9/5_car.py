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
        





class Car(Vehicle):
    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats

    def show_info(self):
        print("--- ข้อมูลรถยนต์ (Car) ---")
        super().show_info()
        print(f"จำนวนที่นั่ง: {self.seats} ที่นั่ง")
