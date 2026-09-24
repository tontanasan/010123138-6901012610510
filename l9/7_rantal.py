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
        # คำนวณจำนวนรอบโปรโมชั่น (ทุกๆ 7 วัน)
        promotion_cycles = days // 7
        # คำนวณเศษวันพักที่เหลือ
        remainder_days = days % 7
        
        # ถ้าเศษวันที่เหลือเกิน 5 วัน ก็คิดเงินแค่ 5 วัน (ตามโปรโมชั่น)
        payable_remainder = remainder_days if remainder_days < 5 else 5
        
        # รวมจำนวนวันที่ต้องจ่ายเงินจริง
        payable_days = (promotion_cycles * 5) + payable_remainder
        
        return self.daily_rate * payable_days
