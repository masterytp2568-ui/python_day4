# 08_traceback_demo.py 

RUN_ERROR_DEMO = False
#RUN_ERROR_DEMO = True

def divide(a, b):
    return a / b

def main():
    x = 10
    y = 0
    print(divide(x, y))

main()

#traceback จะบอก
#ไฟล์และบรรทัดที่ error
#call stack ว่าฟังก์ชั่นใดเรียกฟังก์ชั่นใด
#ชนิด exception และข้อความ error