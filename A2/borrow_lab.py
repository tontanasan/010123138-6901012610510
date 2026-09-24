import json, os

class Equipment:
    def __init__(self, eq_id, name, details, is_borrowed=False, reason=""):
        self.eq_id = eq_id
        self.name = name
        self.details = details
        self.is_borrowed = is_borrowed
        self.reason = reason

class System:
    def __init__(self):
        self.f = "data.json"
        self.items = []
        if os.path.exists(self.f):
            with open(self.f, 'r', encoding='utf-8') as file:
                self.items = [Equipment(**d) for d in json.load(file)]

    def save(self):
        with open(self.f, 'w', encoding='utf-8') as file:
            json.dump([i.__dict__ for i in self.items], file, ensure_ascii=False, indent=2)

    def add(self, name, details):
        new_id = f"{max([int(i.eq_id) for i in self.items]) + 1:03d}" if self.items else "001"
        self.items.append(Equipment(new_id, name, details))
        self.save()
        print(f"เพิ่มสำเร็จ รหัสคือ: {new_id}")

    def delete(self, eq_id):
        for i in self.items:
            if i.eq_id == eq_id:
                if i.is_borrowed:
                    return print("ลบไม่ได้ อุปกรณ์กำลังถูกยืม")
                self.items.remove(i)
                print("ลบสำเร็จ")
                return self.save()
        print("ไม่พบรหัสนี้")

    def show(self, only_borrowed=False):
        for i in self.items:
            if only_borrowed and not i.is_borrowed:
                continue
            status = f"ถูกยืม (เหตุผล: {i.reason})" if i.is_borrowed else "ว่าง"
            print(f"[{i.eq_id}] {i.name} ({i.details}) - {status}")

    def borrow(self, eq_id, reason):
        for i in self.items:
            if i.eq_id == eq_id and not i.is_borrowed:
                i.is_borrowed, i.reason = True, reason
                print("ยืมสำเร็จ")
                return self.save()
        print("ยืมไม่ได้ หรือไม่พบรหัส")

    def ret(self, eq_id):
        for i in self.items:
            if i.eq_id == eq_id and i.is_borrowed:
                i.is_borrowed, i.reason = False, ""
                print("คืนสำเร็จ")
                return self.save()
        print("คืนไม่ได้ หรือไม่พบรหัส")

sys = System()
while True:
    c = input("\n1) ระบบจัดการอุปกรณ์  2) ระบบยืมคืน  0) ออก: ")
    if c == "1":
        while True:
            s = input("\n1.เพิ่ม  2.ลบ  3.ดูรายการ  0.กลับ: ")
            if s == "1": sys.add(input("ชื่อ: "), input("รายละเอียด: "))
            elif s == "2": sys.delete(input("รหัส (เช่น 001): "))
            elif s == "3": sys.show()
            elif s == "0": break
    elif c == "2":
        while True:
            s = input("\n1.ยืม  2.คืน  3.ดูทั้งหมด  4.ดูที่ยืม  0.กลับ: ")
            if s == "1": sys.borrow(input("รหัส: "), input("เหตุผล: "))
            elif s == "2": sys.ret(input("รหัส: "))
            elif s == "3": sys.show()
            elif s == "4": sys.show(True)
            elif s == "0": break
    elif c == "0":
        break