# 07_custom_exception_score.py 

num1 = 100

class InvalidScoreError(Exception):
    pass

def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError("คะแนนต้องอยู่ระหว่าง 0-100")
    return score

def main():
    try:
        score = validate_score(num1)
        print(f"คะแนนถูกต้อง: {score}")
        
    except InvalidScoreError as error:
        print(f"คะแนนไม่ถูกต้อง: {error}")


if __name__ == "__main__":
    main()