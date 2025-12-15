 class CurrencyRates:
    base_currency = "RUB"
    rates = {}

    @classmethod
    def set_base(cls, base):
        cls.base_currency = base

    @classmethod
    def add_rate(cls, currency, value):
        cls.rates[currency] = value

    @classmethod
    def to_base(cls, amount, currency):
        if currency == cls.base_currency:
            return amount
        if currency not in cls.rates:
            raise ValueError(f"Неизвестная валюта: {currency}")
        return amount * cls.rates[currency]

class Money:
    def to_base(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class CodeMoney(Money):
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def to_base(self):
        return CurrencyRates.to_base(self.amount, self.currency)

    def __str__(self):
        base = self.to_base()
        if self.currency == CurrencyRates.base_currency:
            return f"{self.amount:.2f} {self.currency}"
        return f"{self.amount:.2f} {self.currency} = {base:.2f} {CurrencyRates.base_currency}"

class JsonMoney(Money):
    def __init__(self, data):
        self.amount = data["amount"]
        self.currency = data["currency"]

    def to_base(self):
        return CurrencyRates.to_base(self.amount, self.currency)

    def __str__(self):
        base = self.to_base()
        return f"{self.amount:.2f} {self.currency} = {base:.2f} {CurrencyRates.base_currency}"

class LocalMoney(Money):
    def __init__(self, text):
        clean = text.replace(" ", "").replace("₽", "").replace(",", ".")
        self.amount = float(clean)
        self.currency = CurrencyRates.base_currency

    def to_base(self):
        return self.amount

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

class DefaultMoney(Money):
    def __init__(self, amount):
        self.amount = amount
        self.currency = CurrencyRates.base_currency

    def to_base(self):
        return self.amount

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

def total_sum(money_list):
    return sum(m.to_base() for m in money_list)


def find_max(money_list):
    return max(money_list, key=lambda x: x.to_base())


def find_min(money_list):
    return min(money_list, key=lambda x: x.to_base())

def main():
    CurrencyRates.set_base("RUB")
    CurrencyRates.add_rate("USD", 92.5)
    CurrencyRates.add_rate("EUR", 100.0)
    CurrencyRates.add_rate("CNY", 12.3)

    money_list = []

    try:
        money_list.append(CodeMoney(1000, "RUB"))
        money_list.append(CodeMoney(15.5, "USD"))
        money_list.append(JsonMoney({"amount": 200, "currency": "EUR"}))
        money_list.append(LocalMoney("1 000,50 ₽"))
        money_list.append(DefaultMoney(500))
    except ValueError as e:
        print("Ошибка:", e)

    command = "list" 

    if command == "sum":
        total = total_sum(money_list)
        print(f"Total: {total:.2f} {CurrencyRates.base_currency}")

    elif command == "max":
        m = find_max(money_list)
        print(f"Max: {m}")

    elif command == "min":
        m = find_min(money_list)
        print(f"Min: {m}")
    elif command == "list":
        for m in money_list:
            print(m)

    else:
        print("Неизвестная команда")

if __name__ == "__main__":
    main()