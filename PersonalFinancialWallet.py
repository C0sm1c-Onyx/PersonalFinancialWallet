from datetime import datetime as dt


class PersonalWallet:
    number = 1
    class Tracking:
        def __init__(self, category: str, account: int, description: str, create_date: str=None):
            self.id = PersonalWallet.number
            self.create_date = create_date if create_date else dt.strftime(dt.now(), '%Y-%m-%d')
            self.category = category
            self.account = account
            self.description = description
            PersonalWallet.number += 1
            

    def __init__(self, balance:int=0):
        self.balance = balance
        self.trackings = []
        
    def view_balance(self, iterable: list, view_bal=True) -> str:
        s = ''
        for tg in iterable:
            space = " "*(len(str(tg.id))+1)
            s += f'\n{tg.id}.Дата: {tg.create_date}\n{space}Категория: {tg.category}\n{space}Сумма: {tg.account}\n{space}Описание: {tg.description}\n'

        if view_bal:
            return f"Баланс: {self.balance}\n{s}"

        return s

    def insert(self, category: str, account: int, description: str) -> None:
        self.trackings.append(PersonalWallet.Tracking(
            category,
            account,
            description
        ))
        self.configure_balance(category, account)
        save_data(self.view_balance(self.trackings))

    def update(self, id_tg: int, category: str, account: int, description: str) -> None:
        if (id_tg-1) > len(self.trackings):
            raise ValueError("Записи по этому номеру нет")

        entrie = self.trackings[id_tg-1]
        if category:
            entrie.category = category
            self.configure_balance(category if category else entrie.category, int(entrie.account))
        if account:
            self.configure_balance(category if category else entrie.category, abs(int(account) - int(entrie.account)))
            entrie.account = int(account)
        if description:
            entrie.description = description

        save_data(self.view_balance(self.trackings))

    def search(self, s_filter: [str | int]) -> list:
        return filter(lambda tg: s_filter in (tg.create_date, tg.category, str(tg.account)), self.trackings)

    def configure_balance(self, category: str, account: int) -> None:
        if category == "Доход":
            self.balance += account
        else:
            self.balance -= account


def save_data(data: str) -> None:
    with open('data.txt', 'w') as file:
        file.write(f'{data}\n')


def load_data() -> [int, list]:
    with open('data.txt') as file:
        balance = int(file.readline().split(": ")[1])
        trackings, lst = [], []
        for line in file.readlines():
            if len(lst) == 4:
                trackings.append(PersonalWallet.Tracking(*lst[1:], create_date=lst[0]))
                lst.clear()
                
            if not (line == '\n'):
                value = line.strip().split(": ")[1]
                lst.append(value)

            
        return balance, trackings
    
