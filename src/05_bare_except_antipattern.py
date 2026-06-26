# 05_bare_except_antipattern.py 

def demo_not_recommended():
    try:    
        value = 0
        result = 10/value
        print(result)

    except:
        print("เกิดข้อผิดพลาด แต่ไม่รู้ว่าเกิดจากอะไร")

def demo_recommended():
    try:
        value = 0
        result = 10/value
        print(result)
    except ZeroDivisionError:
        print("ตัวหารต้องไม่เป็นศูนย์")
    
    except NameError:
        print("ยังไม่ได้ประกาศตัวแปร value")
    
def main():
    print("=== ตัวอย่างที่ไม่แนะนำ ===")
    demo_not_recommended()
    print("\n=== ตัวอย่างที่แนะนำกว่า ===")
    demo_recommended()


if __name__ == "__main__":
    main()