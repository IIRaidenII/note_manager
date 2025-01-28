notes = [{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'Новая',
          'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
         {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'В процессе',
          'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
         {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'Выполнено',
          'created_date': '20-11-2024', 'issue_date': '26-11-2024'}]
question = input("Введите имя, название, описание или статус для поиска заметки: ")
if (question == notes[0]['username'] or question == notes[0]['title'] or question == notes[0]['content']
    or question == notes[0]['status']):
    note_ = ((notes.pop(0)).values())
    print("Найдена заметка №1:")
    for i in note_:
        print(i)
elif (question == notes[1]['username'] or question == notes[1]['title'] or question == notes[1]['content']
    or question == notes[1]['status']):
    note_ = ((notes.pop(1)).values())
    print("Найдена заметка №2:")
    for i in note_:
        print(i)
elif (question == notes[2]['username'] or question == notes[2]['title'] or question == notes[2]['content']
    or question == notes[2]['status']):
    note_ = ((notes.pop(2)).values())
    print("Найдена заметка №3:")
    for i in note_:
        print(i)
else:
    print("Заметок не найдено :(")
