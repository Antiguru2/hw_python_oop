import datetime as dt
        
date_format = '%d.%m.%Y'
moment = dt.datetime.strptime('08.03.2019', date_format)
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
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        date_format = '%d.%m.%Y'
        formatdate = dt.datetime.strptime(date, date_format)
        self.date = formatdate.date()
        print(f'{self.date}: Я потратил {self.amount} р на {self.comment}!') # Проверка для себя.
    

class Calculator: 
    records = []                   
    def __init__(self, limit):
        self.limit = limit
        print(f'Лимит на день: {self.limit}!') # Проверка для себя.
    
    def add_record(self, record):                
        self.records.append(f'{record.amount}, {record.date}')    # Я не понимаю, что я должен ввести, что бы напечатать свойства R1              
        #print(self.records)

    def get_today_stats(self):
        summ_day_amount = 0
        for n in self.records:
            amount_date = n.split(', ')
            asd = int(amount_date[0])                 # Я правильно рассуждаю?
            if str(day) == amount_date[-1] :
                summ_day_amount += asd

                #print(f'Сегодня потрачено: {summ_day_amount} р!!!') 
        print(f'Сегодня потрачено: {summ_day_amount} р!!!') 
                                       
    def get_week_stats(self):
        summ_day_amount = 0 
        for n in self.records:            
            amount_date = n.split(', ')
            #summ_day_amount += amount_date[0]

        #print(f'За неделю  потрачено: {summ_day_amount} р!!!')
        
    
Calculator1 = Calculator(1000)
    



# для CashCalculator 
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси", date="08.03.2019")

# для CaloriesCalculator
#r4 = Record(amount=1186, comment="Кусок тортика. И ещё один.", date="24.02.2019")
#r5 = Record(amount=84, comment="Йогурт.", date="23.02.2019")
#r6 = Record(amount=1140, comment="Баночка чипсов.", date="24.02.2019")


Calculator1.add_record(r1)
Calculator1.add_record(r2)
Calculator1.add_record(r3)

Calculator1.get_today_stats()

Calculator1.get_week_stats()
