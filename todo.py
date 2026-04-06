# todo_list.py
# 日常学习待办清单工具
import json
import os

TODO_FILE = 'todo.json'

def load_todo():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_todo(todos):
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)

def main():
    todos = load_todo()
    print("=== 个人待办清单 ===")
    while True:
        print("\n1. 查看待办  2. 添加待办  3. 标记完成  0. 退出")
        c = input("请选择：")
        if c == '1':
            for i, t in enumerate(todos, 1):
                status = "√ 已完成" if t['done'] else "□ 未完成"
                print(f"{i}. {t['content']}  {status}")
        elif c == '2':
            content = input("输入待办内容：")
            todos.append({"content": content, "done": False})
            save_todo(todos)
            print("添加成功")
        elif c == '3':
            idx = int(input("输入完成的序号：")) - 1
            if 0 <= idx < len(todos):
                todos[idx]['done'] = True
                save_todo(todos)
                print("已标记完成")
        elif c == '0':
            break

if __name__ == '__main__':
    main()