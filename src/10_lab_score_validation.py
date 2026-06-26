# 10_lab_score_validation.py 

def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("คะแนนต้องอยู่ระหว่าง 0-100")
    return score

def ask_score():
    while True:
        try:
            raw_score = input("กรอกคะแนน 0-100: ")
            return validate_score(float(raw_score))
        except ValueError as error:
            print(f"ลองใหม่: {error}")

def main():
    score = ask_score()

    if score >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"

    print(f"คะแนนที่บันทึก: {score}")
    print(f"ผลลัพธ์: {result}")

if __name__ == "__main__":
    main()