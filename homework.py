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
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date:
            formatdate = dt.datetime.strptime(date, date_format)
            self.date = formatdate.date()
        else:
            self.date = dt.datetime.now().date()

    def __repr__(self):
        return str(self.amount)

        
class Calculator: 
                     
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


class CaloriesCalculator(Calculator): 
    def get_calories_remained(self): 
        
        if self.get_today_stats() < self.limit:
            balance_for_the_day = self.limit - self.get_today_stats()
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance_for_the_day} кКал.'
        else:
            return f'Хватит жрать!!!'
            
        

    

сash_сalculator = CashCalculator(1000)
calories_calculator = CaloriesCalculator(900)


сash_сalculator.add_record(Record(amount=900, comment="бар в Танин др", date="27.03.2021"))
сash_сalculator.add_record(Record(amount=200, comment="бар в Танин др"))
calories_calculator.add_record(Record(amount=800, comment="бар в Танин др"))

#print(сash_сalculator.get_today_cash_remained("usd"))
print(calories_calculator.get_calories_remained())


