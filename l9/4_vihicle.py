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

    def calculate_rental_cost(self, days):
        return self.daily_rate * days
