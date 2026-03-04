"""
To-Do List 관리 프로그램
- 할 일 추가, 완료, 삭제, 조회 기능
"""

import json
import os

TODO_FILE = "todos.json"


def load_todos():
    """파일에서 할 일 목록을 불러옵니다."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_todos(todos):
    """할 일 목록을 파일에 저장합니다."""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def show_todos(todos):
    """할 일 목록을 출력합니다."""
    if not todos:
        print("\n📋 할 일이 없습니다!\n")
        return
    print("\n📋 할 일 목록:")
    print("-" * 40)
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo["done"] else "⬜"
        print(f"  {i}. {status} {todo['task']}")
    print("-" * 40)
    print()


def add_todo(todos):
    """새로운 할 일을 추가합니다."""
    task = input("추가할 할 일을 입력하세요: ").strip()
    if task:
        todos.append({"task": task, "done": False})
        save_todos(todos)
        print(f"✅ '{task}' 추가 완료!")
    else:
        print("❌ 빈 할 일은 추가할 수 없습니다.")


def complete_todo(todos):
    """할 일을 완료 처리합니다."""
    show_todos(todos)
    if not todos:
        return
    try:
        num = int(input("완료할 항목 번호: "))
        if 1 <= num <= len(todos):
            todos[num - 1]["done"] = True
            save_todos(todos)
            print(f"🎉 '{todos[num - 1]['task']}' 완료!")
        else:
            print("❌ 잘못된 번호입니다.")
    except ValueError:
        print("❌ 숫자를 입력해주세요.")


def delete_todo(todos):
    """할 일을 삭제합니다."""
    show_todos(todos)
    if not todos:
        return
    try:
        num = int(input("삭제할 항목 번호: "))
        if 1 <= num <= len(todos):
            removed = todos.pop(num - 1)
            save_todos(todos)
            print(f"🗑️ '{removed['task']}' 삭제 완료!")
        else:
            print("❌ 잘못된 번호입니다.")
    except ValueError:
        print("❌ 숫자를 입력해주세요.")


def main():
    """메인 함수 - 메뉴를 표시하고 사용자 입력을 처리합니다."""
    print("=" * 40)
    print("  📝 To-Do List 관리 프로그램")
    print("=" * 40)

    todos = load_todos()

    while True:
        print("\n[1] 할 일 보기  [2] 추가  [3] 완료  [4] 삭제  [0] 종료")
        choice = input("선택: ").strip()

        if choice == "1":
            show_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "0":
            print("👋 프로그램을 종료합니다. 안녕!")
            break
        else:
            print("❌ 올바른 메뉴를 선택해주세요.")


if __name__ == "__main__":
    main()