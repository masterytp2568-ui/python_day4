# 25_cli_line_counter.py 

import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description="นับบรรทัดและตัวอักษรในไฟล์")
    parser.add_argument("input_file", help="ไฟล์ข้อความ UTF-8")
    return parser.parse_args()

def main():
    args = parse_args()
    path = Path(args.input_file)

    try:
        text = path.read_text(encoding="utf-8")
    
    except FileNotFoundError:
        print(f"[ERROR] ไม่พบไฟล์: {path}")
        raise SystemExit(1)
    except UnicodeDecodeError:
        print("[ERROR] อ่านไฟล์ไม่ได้ กรุณาตรวจ encoding")
        raise SystemExit(1)
    
    lines = text.splitlines()
    print(f"ไฟล์: {path}")
    print(f"จำนวนบรรทัด: {len(lines)}")
    print(f"จำนวนตัวอักษร: {len(text)}")


if __name__ == "__main__":
    main()