question = input("Вы действительно хотите сменить даты создания и истечения заметки ? ")
if question == "Нет":
    print("Смена даты и истечения заметки отменена ")
if question == "Да":
    created_date = str(input("Введите новую дату создания (День, месяц, год; через .) "))
    issue_date = str(input("Введите новую дату истечения (День, месяц, год; через .) "))
    created_date1 = created_date[0:5]
    issue_date1 = issue_date[0:5]
    print("Готово! Теперь, ваша заметка создана:", created_date1, ", а дата истечения:", issue_date1)

