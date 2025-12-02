 class Money:
    rates = {} 
    base_curr = ""
    
    def __init__(self, amount, currency=None):
        self.amount = amount
        self.currency = currency if currency else Money.base_curr
    
    def to_base(self):
        if self.currency == Money.base_curr:
            return self.amount
        return self.amount * Money.rates.get(self.currency, 0)
    
    def __str__(self):
        base_val = self.to_base()
        if self.currency == Money.base_curr:
            return f"{self.amount:.2f} {self.currency}"
        return f"{self.amount:.2f} {self.currency} = {base_val:.2f} {Money.base_curr}"

Money.base_curr = "RUB"
Money.rates = {"USD": 92.5, "EUR": 100.0}

sums = [
    Money(1000, "RUB"),               
    Money(15.5, "USD"),               
    Money(200, "EUR"),                
    Money(1000.50, "RUB"),            
    Money(500)                        
]

print("Список всех сумм:")
for s in sums:
    print(f"  {s}")

print(f"\nОбщая сумма: {sum(s.to_base() for s in sums):.2f} {Money.base_curr}")

max_s = max(sums, key=lambda x: x.to_base())
print(f"\nМаксимальная: {max_s.amount:.2f} {max_s.currency} = {max_s.to_base():.2f} {Money.base_curr}")

min_s = min(sums, key=lambda x: x.to_base())
print(f"Минимальная:  {min_s.amount:.2f} {min_s.currency} = {min_s.to_base():.2f} {Money.base_curr}") 