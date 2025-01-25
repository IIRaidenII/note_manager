note = {'username': 'Райден', 'title': 'Учеба', 'content': 'Расписание занятий',
        'status': 'Активно', 'created_date': '16.06.2024', 'issue_date': '16.06.2025'}
print(note)
question = input("Вы хотите сменить данные заметки? ")
if question == "Да":
    question_ = input("Введите поле для замены (username, title, content, status, issue_date): ")
    if question_ == "username":
        note['username'] = input(str("Введите новое имя: "))
        print(note)
    elif question_ == "title":
        note['title'] = input(str("Введите новое название для заметки: "))
        print(note)
    elif question_ == "content":
        note['content'] = input(str("Введите новое описание: "))
        print(note)
    elif question_ == "status":
        note['status'] = input(str("Введите новое статус заметки: "))
        print(note)
    elif question_ == "issue_date":
        note['issue_date'] = input(str("Введите новую дату истечения заметки заметки (День.месяц.год): "))
        print(note)
elif question == "Нет":
    print("Изменение заметки отменено")
else:
    print("Некорректный ввод")


