import json

class Money:
    def init(self, amount, currency, rates):
        self.amount = float(amount)
        self.currency = currency
        self.rates = rates
    
    def to_base(self):
        if self.currency == "RUB":
            return self.amount
        if self.currency in self.rates:
            return self.amount * self.rates[self.currency]
        else:
            raise ValueError(f"Нет курса для валюты {self.currency}")
    
    def str(self):
        base = self.to_base()
        if self.currency == "RUB":
            return f"{self.amount:.2f} RUB"
        else:
            return f"{self.amount:.2f} {self.currency} = {base:.2f} RUB"

rates = {"RUB": 1.0}
print("Введите курсы валют (формат: USD 92.5), пустая строка - конец:")
while True:
    line = input().strip()
    if not line:
        break
    try:
        parts = line.split()
        if len(parts) != 2:
            print("Ошибка формата, пропускаю")
            continue
        code, rate = parts
        rates[code] = float(rate)
    except:
        print("Ошибка ввода, пропускаю")

print("Курсы установлены.")
money_list = []

print("Вводите суммы (пустая строка - конец):")
while True:
    line = input().strip()
    if not line:
        break
    
    try:
        if line.startswith("code"):
            parts = line.split()
            if len(parts) != 3:
                print("Ошибка формата code")
                continue
            _, amount, curr = parts
            money_list.append(Money(amount, curr, rates))
        
        elif line.startswith("json"):
            json_str = line[5:]
            data = json.loads(json_str)
            money_list.append(Money(data["amount"], data["currency"], rates))
        
        elif line.startswith("local"):
            rest = line[6:].replace(" ", "").replace(",", ".")
            if "₽" in rest:
                amount = rest.replace("₽", "")
                money_list.append(Money(amount, "RUB", rates))
            else:
                print("Неизвестная валюта в local")
        
        elif line.startswith("default"):
            amount = line.split()[1]
            money_list.append(Money(amount, "RUB", rates))
        
        else:
            print("Неизвестный формат")
    
    except Exception as e:
        print(f"Ошибка: {e}")

print("Введите команду (sum/max/min/list):")
cmd = input().strip()

if cmd == "sum":
    total = sum(m.to_base() for m in money_list)
    print(f"Total: {total:.2f} RUB")

elif cmd == "max":
    if money_list:
        max_money = max(money_list, key=lambda x: x.to_base())
        print(f"Max: {max_money}")
    else:
        print("Список пуст")

elif cmd == "min":
    if money_list:
        min_money = min(money_list, key=lambda x: x.to_base())
        print(f"Min: {min_money}")
    else:
        print("Список пуст")

elif cmd == "list":
    for m in money_list:
        print(m)
else:
    print("Неизвестная команда") 