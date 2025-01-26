from datetime import date
notes = []
notes_numbers = []
display_notes = [notes]
print ("Сейчас у вас 0 заметкок")
question = input("Хотите добавить заметку? ")
if question == "Да":
    all_notes = int(input("Сколько заметок хотите создать? "))
    for i in range(1, all_notes + 1):
        notes_numbers.append(i)
    for i in range(all_notes):
        name = str(input("Введите ваше имя: "))
        title = str(input("Введите название заметки: "))
        content = str(input("Введите описание: "))
        status = str(input("Введите статус: "))
        date_created = str(date.today())
        date_issue = str(input("Введите дату дедлайна (Год, месяц, день):"))
        notes.append(['Заметка', notes_numbers[i]])
        notes.append(name)
        notes.append(title)
        notes.append(content)
        notes.append(status)
        notes.append(date_created)
        notes.append(date_issue)
        notes.append("")
    for i in notes:
        print(i)
elif question == "Нет":
    print ("У вас нет сохранённых заметок")
else:
    print("Некорректный ввод")