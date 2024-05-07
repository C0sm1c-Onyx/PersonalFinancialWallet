from PersonalFinancialWallet import *


pw = PersonalWallet()
try:
    pw.balance, pw.trackings = load_data()
except FileNotFoundError:
    pass
        
while True:
    x = input("Выберите действие: \n1.Вывод баланса\n2.Добавить запись\n3.Редактировать запись\n4.Поиск записи\n5.Выйти\n")
    if x == "1":
        print(pw.view_balance(pw.trackings))
        input('Нажмите "Enter", чтобы продолжить')
            
    elif x == "2":
        category = input("Введите категорию: ").title()
        account = int(input("Введите сумму: "))
        description = input("Введите описание: ")
        pw.insert(category, account, description)
        save_data(pw.view_balance(pw.trackings))
        input("Добавлено")
            
    elif x == "3":
        id_tg = int(input("Введите номер записи: "))
        print("Оставьте поле пустым, если не собираетесь изменять")
        category = input("Введите категорию: ")
        account = input("Введите сумму: ")
        description = input("Введите описание: ")
        pw.update(id_tg, category, account, description)
        save_data(pw.view_balance(pw.trackings))
        input("Обновлено")
            
    elif x == "4":
        search_filter = input("Поиск (Категория, Сумма или Дата): ")
        iterable = pw.search(search_filter)
        print(pw.view_balance(iterable, view_bal=False))
        input('Нажмите "Enter", чтобы продолжить')
            
    elif x == "5":
        break
        
    else:
        print("(!) Введите цифру от 1 до 5")
