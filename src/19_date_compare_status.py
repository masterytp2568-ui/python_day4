# 19_date_compare_status.py 

from datetime import date

today = date.today()
due_date = date(2026, 6, 30)

if due_date < today:
    status = "overdue"
elif due_date == today:
    status = "due today"
else:
    status = "upcoming"

print(f"วันนี้: {today}")
print(f"กำหนดส่ง: {due_date}")
print(f"สถานะ: {status}")