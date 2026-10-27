import cases
import storage
def show_cases(items):
    if len(items) == 0:
        print("Журнал пуст")
    else:
        for item in items:
            print(item["id"], item["title"], item["status"])
def read_id():
    text = input("Введите ID: ").strip()
    try:
        number = int(text)
    except ValueError:
        print("ID должен быть целым числом")
        return None
    if number <= 0:
        print("ID должен быть больше 0")
        return None
    else:
        return number
def main():
    items = storage.load_cases("cases.json")
    if items is None:
        print("ОШИБКА!!!")
        return
    while True:
        print(" ╔════════════════════════════════╗")
        print(" ║1.          Список              ║")
        print(" ║2.          Добавить            ║")
        print(" ║3.          Результат           ║")
        print(" ║4.          Сводка              ║")
        print(" ║5.          Сохранить           ║")
        print(" ║0.          Выход               ║")
        print(" ╚════════════════════════════════╝")
        a = input("Выберите: ").strip()
        if a == "0":
            break
        elif a == "1":
            show_cases(items)
        elif a == "2":
            title = input("Введите название: ")
            new_id = cases.add_case(items, title)
            if new_id is None:
                print("Название слишком короткое")
            else:
                print("Добавлено, ID:", new_id)
        elif a == "3":
            case_id = read_id()
            if case_id is not None:
                status = input("Статус (pending/pass/fail):")
                answer = cases.set_result(items, case_id, status)
                print(answer)
        elif a == "4":
            print(cases.summarize(items))
        elif a == "5":
            save_answer = input("Сохранить? да/нет: ").strip().lower()
            if save_answer == "да":
                ok = storage.save_cases("cases.json", items)
                if ok is True:
                    return
                else:
                    print("Ошибка записи")
            elif save_answer == "нет":
                return
        else:
            print("Неизвестная команда! Попробуйте снова.")
if __name__ == "__main__":
    main()