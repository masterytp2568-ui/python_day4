# 06_raise_discount_validation.py 

def calculate_discount(price, percent):
    if price < 0:
        raise ValueError("price ต้องไม่ติดลบ")
    if not 0 <= percent <= 100:
        raise ValueError("percent ต้องอยู่ระหว่าง 0-100")
    return price * percent / 100

try:
    price = 1000
    discount = 100
    print("ราคาเต็ม: ", price)
    print("ส่วนลด: ", discount, " %")
    print("ค่าส่วนลด: ",calculate_discount(price, discount))

except ValueError as error:
    print(f"ข้อมูลไม่ถูกต้อง: {error}")
