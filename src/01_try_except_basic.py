# 01_try_except_basic.py

try:
    price = float(input("ราคาสินค้า: "))
    quantity = int(input("จำนวน: "))
    total = price * quantity
    print(f"ยอดรวม = {total:.2f} บาท")

except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")

def main():
    if __name__ == "__main__":
        main()
