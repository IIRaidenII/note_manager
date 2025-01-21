from datetime import date
from datetime import datetime
date_ = str(date.today())
print("Сегодня:", date_)
question = str(input("Введите дату истечения вашей замекти (Формат: Год-месяц-день): "))
if date_ < question:
    date_ = datetime.strptime(date_, '%Y-%m-%d')
    question = datetime.strptime(question, '%Y-%m-%d')
    result = (question-date_).days
    print("Ваш дедлайн истечёт через", result, "дней")
if date_ == question:
    print("Ваш Дедлайн: Сегодня")
if date_ > question:
    date_ = datetime.strptime(date_, '%Y-%m-%d')
    question = datetime.strptime(question, '%Y-%m-%d')
    result = (date_ - question).days
    print("Ваш Дедлайн истёк", result,"дней назад")


