import datetime as dt
        
date_format = '%d.%m.%Y'
moment = dt.datetime.strptime('16.12.2019', date_format)
#print(moment)
# напечатает что-то вроде 2019-12-16 00:00:00        
day = moment.date()
#print(day)
# напечатает дату: 2019-12-16        
now = dt.datetime.now()
#print(now)
# напечатает время на текущий момент в формате: 2019-01-31 13:33:27.506227        
#print(now.date()) 
# напечатает текущую дату: 2019-01-31

class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date
        print(f'Созданна запись: {self.comment}!') # Проверка для себя.
    

class Calculator:                    
    def __init__(self, limit):
        self.limit = limit
        print(f'Созданна запись: {self.limit}!') # Проверка для себя.
    
    def add_record(self, Record):
        records = []
        records.append(Record)

        print(Record)
    
Calculator1 = Calculator(1000)
    



# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")

Calculator1.add_record(r1)