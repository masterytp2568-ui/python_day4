# 27_personal_report_solution.py 
# Mini Project: Personal CL Report Solution tools
# Exception Handling + Date & Time + Command Line Script

import argparse
import csv
from collections import Counter
from datetime import date, datetime
from pathlib import Path

DATE_FORMAT = "%d/%m/%Y"

def parse_args():
    parser = argparse.ArgumentParser(description="สรุปรายการงานตามกำหนดส่ง")
    parser.add_argument("input_file", help="ไฟล์ CSV รายการงาน")
    parser.add_argument("--output", default="output/report.txt", help="ไฟล์รายงานผลลัพธ์")
    parser.add_argument("--today", default=None, help="วันที่อ้างอิงสำหรับทดสอบ รูปแบบ dd/mm/yyyy")
    return parser.parse_args()

def parse_today(today_text):
    if today_text is None:
        return date.today()

    return datetime.strptime(today_text, DATE_FORMAT).date()

def get_task_status(due_date_text, today):
    try:
        due_date = datetime.strptime(due_date_text, DATE_FORMAT).date()
    except ValueError:
        return "invalid", None
    
    diff_days = (due_date-today).days

    if diff_days < 0:
        return "overdue", diff_days
    if diff_days == 0:
        return "due today", diff_days

    return "upcoming", diff_days

def read_tasks(path):
    tasks = []
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row)
    return tasks

def build_report_lines(tasks, today):
    lines = []
    summary = Counter()

    for task in tasks:
        title = task.get("title", "ไม่ระบุชื่อ").strip() or "ไม่ระบุชื่อ"
        due_date_text = task.get("due_date","").strip()
        status, days = get_task_status(due_date_text, today)
        summary[status] += 1 

        if status == "invalid":
            detail = "วันที่ไม่ถูกต้อง"
        elif days < 0:
            detail = f"เลยกำหนด {-days} วัน"
        elif days == 0:
            detail = "ครบกำหนดวันนี้" 
        else:
            detail = f"เหลืออีก {days} วัน"
    
        lines.append(f"- {title} | due_date={due_date_text} | status={status} | {detail}")
    
    lines.append("")
    lines.append("สรุปจำนวนตามสถานะ")
    for status in ["overdue","due_today","upcoming","invalid"]:
        lines.append(f"- {status}: {summary[status]}")


    return lines

def write_report(output_path, lines):
    output_path.parent.mkdir(parents=True,exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = [f"Task Report - {timestamp}","=" * 40]
    content.extend(lines)
    output_path.write_text("\n".join(content), encoding="utf-8")


def main():
    args = parse_args()
    input_path = Path(args.input_file)
    output_path = Path(args.output)

    try:
        today = parse_today(args.today)
    
    except ValueError:
        print("[ERROR] --today ต้องอยู่ในรูปแบบ dd/mm/yyyy เช่น 25/06/2026")
        raise SystemExit(1)
    
    try:
        tasks = read_tasks(input_path)
    
    except FileNotFoundError:
        print(f"[ERROR] ไม่พบไฟล์: {input_path}")
        raise SystemExit(1)
    except UnicodeDecodeError:
        print("[ERROR] อ่านไฟล์ไม่ได้ กรุณาตรวจ endoding ให้เป็น UTF-8")
        raise SystemExit(1)
    
    lines = build_report_lines(tasks, today)
    write_report(output_path, lines)
    print(f"สร้างรายงานแล้ว: {output_path}")


if __name__ == "__main__":
    main()
