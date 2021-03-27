import datetime as dt
        
date_format = '%d.%m.%Y'
moment = dt.datetime.strptime('08.03.2019', date_format)
#print(moment)
# напечатает что-то вроде 2019-12-16 00:00:00        
day = moment.date()
#print(day)
# напечатает дату: 2019-12-16        
now = dt.datetime.now()
nowdate = now.date()
#print(now)
# напечатает время на текущий момент в формате: 2019-01-31 13:33:27.506227        
#print(now.date()) 
# напечатает текущую дату: 2019-01-31

class Record:
    def __init__(self, amount, comment, date='nowdate'):
        self.amount = amount
        self.comment = comment
        formatdate = dt.datetime.strptime(date, date_format)
        self.date = formatdate.date()
        
class Calculator: 
    records = []                 
    def __init__(self, limit):
        self.limit = limit
    
    def add_record(self, record):                
        self.records.append(record)    

    def get_today_stats(self):
        summ_day_amount = 0
        for object_record in self.records:         
            if now.date() == object_record.date:
                summ_day_amount += object_record.amount
        return summ_day_amount
                                      
    def get_week_stats(self):
        summ_weekday_amount = 0 
        one_week_ago = now.date() - dt.timedelta(days=7)
        for object_record in self.records:  
            if one_week_ago <= object_record.date: 
                summ_weekday_amount += object_record.amount 
        return summ_weekday_amount 
          
        
class CashCalculator(Calculator): 
    def __init__(self, type_of_currency):
        self.type_of_currency = type_of_currency
    def get_today_stats(seif, type_of_currency): 
        currency_multiplier = сash_сalculator.get_today_cash_remained(type_of_currency)
        if Calculator1.get_today_stats() < Calculator1.limit:
            balance_for_the_day = Calculator1.limit - Calculator1.get_today_stats()
            print(f'На сегодня осталось {round((balance_for_the_day/currency_multiplier), 2)} {type_of_currency}...')

        elif Calculator1.get_today_stats() == Calculator1.limit:
            print(f'Денег нет но, вы держитесь...')

        else:
            balance_for_the_day = Calculator1.get_today_stats() - Calculator1.limit
            print(f'Денег нет, держись: твой долг -{round((balance_for_the_day/currency_multiplier), 2)} {type_of_currency}')


        print(f'За неделю потрачено: {round((Calculator1.get_week_stats()/currency_multiplier), 2)} {type_of_currency}!!!')  

    def get_today_cash_remained(saif, rate):
        if rate == 'USD':
            return 85
        elif rate == 'EUR':
            return 90
        else:
            return 0              #conventional_units
            


class CaloriesCalculator(Calculator): 
    def get_today_stats(seif): 
        if Calculator2.get_today_stats() < Calculator2.limit:
            balance_for_the_day = Calculator2.limit - Calculator2.get_today_stats()
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance_for_the_day} кКал.')

        else:
            print(f'Хватит жрать!!!')

        print(f'За неделю сожранно: {Calculator2.get_week_stats()} кКал!!!') 

    
Calculator1 = Calculator(1000)
Calculator2 = Calculator(1000)
сash_сalculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(1000)
# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг", date="24.03.2021")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="23.03.2021")
r3 = Record(amount=691, comment="Катание на такси", date="24.03.2021")
r4 = Record(amount=654, comment="Питание на работе", date="22.03.2021")
r5 = Record(amount=1566, comment="Ресторан", date="21.03.2021")
r6 = Record(amount=3000, comment="Питание на работе", date="20.03.2021")
r7 = Record(amount=389, comment="Подарок", date="19.03.2021")
r8 = Record(amount=666, comment="Питание на работе", date="18.03.2021")
# для CaloriesCalculator
rе1 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
rе2 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
rе3 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")
rе4 = Record(amount=1566, comment="Бургер", date="21.03.2021")
rе5 = Record(amount=1990, comment="Борщ", date="20.03.2021")
rе6 = Record(amount=56, comment="Пикасе", date="19.03.2021")
rе7 = Record(amount=400, comment="Том ям", date="18.03.2021")

Calculator1.add_record(r1)
Calculator1.add_record(r2)
Calculator1.add_record(r3)
Calculator1.add_record(r4)
Calculator1.add_record(r5)
Calculator1.add_record(r6)
Calculator1.add_record(r7)
Calculator2.add_record(rе1)
Calculator2.add_record(rе2)
Calculator2.add_record(rе3)
Calculator2.add_record(rе4)
Calculator2.add_record(rе5)
Calculator2.add_record(rе6)
Calculator2.add_record(rе7)




сash_сalculator.get_today_stats('EUR')
calories_calculator.get_today_stats()

