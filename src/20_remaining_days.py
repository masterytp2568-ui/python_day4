# 20_remaining_days.py 

from datetime import date

today = date.today()
deadline = date(2026, 7 ,15)
remaining_days = (deadline - today).days

if remaining_days < 0:
    print(f"เลยกำหนดแล้ว {-remaining_days} วัน")
else:
    print(f"เหลืออีก {remaining_days} วัน")