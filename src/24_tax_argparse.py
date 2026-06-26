# 24_tax_argparse.py 

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="คำนวณภาษีสินค้า")
    parser.add_argument("price", type=float, help="ราคาสินค้า")
    parser.add_argument("--tax",type=float,default=7.0, help="อัตราภาษี percent")
    return parser.parse_args()

def main():
    args = parse_args()
    tax_amount = args.price * args.tax / 100
    total = args.price + tax_amount

    print(f"ภาษี = {tax_amount:.2f}")
    print(f"รวม = {total:.2f}")

if __name__ == "__main__":
    main()