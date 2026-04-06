# budget_record.py
# 日常记账小工具
import json
import os
from datetime import datetime

DATA_FILE = 'budget.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    records = load_data()
    print("=== 个人日常记账工具 ===")
    while True:
        print("\n1. 记一笔支出  2. 查看记录  3. 统计总支出  0. 退出")
        c = input("选择操作：")
        if c == '1':
            money = float(input("金额："))
            note = input("备注（吃饭/购物等）：")
            records.append({
                "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "money": money,
                "note": note
            })
            save_data(records)
            print("记录成功")
        elif c == '2':
            for r in records:
                print(f"{r['time']} | {r['money']}元 | {r['note']}")
        elif c == '3':
            total = sum(r['money'] for r in records)
            print(f"当前总支出：{total:.2f} 元")
        elif c == '0':
            break

if __name__ == '__main__':
    main()