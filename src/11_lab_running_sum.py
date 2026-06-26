# 11_lab_running_sum.py 
# LAB2 running sum

def main():
    total = 0.0
    count = 0

    while True:
        text = input("กรอกตัวเลข หรือ q เพื่อจบ: ")

        if text.lower() == "q":
            break

        try:
            number = float(text)
            
        except ValueError:
            print("ข้ามรายการนี้: กรุณากรอกตัวเลข")
            continue

        total += number
        count += 1
    
    print("จบโปรแกรม")
    print(f"จำนวนข้อมูล = {count}")
    print(f"ผลรวม = {total:.2f}")

    if count > 0:
        print(f"ค่าเฉลี่ย: {total / count:.2f}")
    else:
        print("ยังไม่มีข้อมูล จึงคำนวณค่าเฉลี่ยไม่ได้")
    
if __name__ == "__main__":
    main()
