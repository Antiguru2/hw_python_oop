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
<<<<<<< HEAD
        if date:
            formatdate = dt.datetime.strptime(date, date_format)
            self.date = formatdate.date()
        else:
            self.date = dt.datetime.now().date()

    def __repr__(self):
        return str(self.amount)

        
class Calculator: 
                     
=======
        formatdate = dt.datetime.strptime(date, date_format)
        self.date = formatdate.date()
        
class Calculator: 
    records = []                 
>>>>>>> 1bfdaeff7aad41b174dedc66b129ac84fa2fdf5b
    def __init__(self, limit):
        self.limit = limit
        self.records = []
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
<<<<<<< HEAD
    USD_RATE = 85
    EURO_RATE = 90
    
    def get_today_cash_remained(self, currency): 
        rate_dict = {
            'rub': {
                'name': 'руб',
                'rate': 1
            },
            'usd': {
                'name': 'USD',
                'rate': self.USD_RATE
            },
            'eur': {
                'name': 'Euro',
                'rate': self.EURO_RATE
            }
            
        }
        balance_for_the_day = self.limit - self.get_today_stats()
        try:
            converted_balance_for_the_day = round(balance_for_the_day / rate_dict[currency]['rate'], 2)
        except KeyError:
            return f'Ошибка: KeyError. Валюта, { currency } ,не найдена!'

        # curr_rate = rate_dict.get(currency)
        # if curr_rate:
        #     converted_balance_for_the_day = round(balance_for_the_day / curr_rate['rate'], 2)
        # else:        
        #     return f'Ошибка: KeyError. Валюта, { currency } ,не найдена!'


        if self.get_today_stats() < self.limit:
            
            return f'На сегодня осталось { converted_balance_for_the_day  } { rate_dict[currency]["name"] }...'

        elif self.get_today_stats() == self.limit:
            return f'Денег нет но, вы держитесь...'
        else:
            return f'Денег нет, держись: твой долг { converted_balance_for_the_day } { rate_dict[currency]["name"] }'      
=======
    def __init__(self, type_of_currency):
        self.type_of_currency = type_of_currency
    def get_today_stats(seif, type_of_currency): 
        currency_multiplier = сash_сalculator.get_today_cash_remained(type_of_currency)
        if Calculator1.get_today_stats() < Calculator1.limit:
            balance_for_the_day = Calculator1.limit - Calculator1.get_today_stats()
            print(f'На сегодня осталось {round((balance_for_the_day/currency_multiplier), 2)} {type_of_currency}...')
>>>>>>> 1bfdaeff7aad41b174dedc66b129ac84fa2fdf5b


class CaloriesCalculator(Calculator): 
    def get_calories_remained(self): 
        
        if self.get_today_stats() < self.limit:
            balance_for_the_day = self.limit - self.get_today_stats()
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance_for_the_day} кКал.'
        else:
<<<<<<< HEAD
            return f'Хватит жрать!!!'
            
        
=======
            balance_for_the_day = Calculator1.get_today_stats() - Calculator1.limit
            print(f'Денег нет, держись: твой долг -{round((balance_for_the_day/currency_multiplier), 2)} {type_of_currency}')
>>>>>>> 1bfdaeff7aad41b174dedc66b129ac84fa2fdf5b

    

<<<<<<< HEAD
сash_сalculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(900)
=======
        print(f'За неделю потрачено: {round((Calculator1.get_week_stats()/currency_multiplier), 2)} {type_of_currency}!!!')  

    def get_today_cash_remained(saif, rate):
        if rate == 'USD':
            return 85
        elif rate == 'EUR':
            return 90
        else:
            return 0              #conventional_units
            

>>>>>>> 1bfdaeff7aad41b174dedc66b129ac84fa2fdf5b


сash_сalculator.add_record(Record(amount=900, comment="бар в Танин др", date="27.03.2021"))
сash_сalculator.add_record(Record(amount=200, comment="бар в Танин др"))
calories_calculator.add_record(Record(amount=800, comment="бар в Танин др"))

#print(сash_сalculator.get_today_cash_remained("usd"))
print(calories_calculator.get_calories_remained())


<<<<<<< HEAD
=======
    
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

>>>>>>> 1bfdaeff7aad41b174dedc66b129ac84fa2fdf5b
