# 09_read_number_loop.py 

def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("กรุณากรอกตัวเลขใหม่อีกครั้ง")
            # ถ้ากรอกไม่ถูกจะรอรับค่าใหม่จนกว่าจะถูกถึงจะทำงานต่อ
            
price = read_number("ราคาสินค้า: ")
quantity = read_number("จำนวน: ")
print(f"ยอดรวม = {price * quantity:.2f}")

