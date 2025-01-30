
def create_note():
    note = []
    username = note.append(input("Введите имя: "))
    title = note.append(input("Введите заголовок: "))
    content = note.append(input("Введите описание: "))
    status = note.append(input("Введите статус (Новая, в процессе, выполнено): "))
    created_date = note.append(input("Дата создания (День.месяц.год): "))
    issue_date = note.append(input("Дата дедлайна (День.месяц.год): "))
    for i in note:
        print(i)
    print()
    for i in notes:
        print(i)

def display_notes ():
    for i in notes:
        print(i)

def update_note():
    question1 = input("Введите поле для замены (Имя, Название, Описание, Статус, Дата создания, Дата истечения): ")
    if question1 == "Имя":
        notes[0] = input("Введите новое имя: ")
        for i in notes:
            print(i)
    elif question1 == 'Название':
        notes[1] = input("Введите новое название для заметки: ")
        for i in notes:
            print(i)
    elif question1 == 'Описание':
        notes[2] = input("Введите новое описание: ")
        for i in notes:
            print(i)
    elif question1 == 'Статус':
        notes[3] = input("Введите новое статус заметки: ")
        for i in notes:
            print(i)
    elif question1 == "Дата создания":
        notes[4] = input("Введите новую дату истечения заметки заметки (День.месяц.год): ")
        for i in notes:
            print(i)
    elif question1 == "Дата истечения":
        notes[5] = input("Введите новую дату истечения заметки заметки (День.месяц.год): ")
        for i in notes:
            print(i)
    else:
        print("Некорректный ввод")

def delete_note():
    question2 = input("Вы уверены, что хотите удалить заметку?")
    if question2 == "Да":
        notes.remove('Алексей')
        notes.remove('Список покупок')
        notes.remove('Купить продукты на неделю')
        notes.remove('Новая')
        notes.remove('27-11-2024')
        notes.remove('30-11-2024')
        print("Заметка удалена!")
    elif question2 == "Нет":
        print("Удаление отменено")
    else:
        print("Некорректный ввод")

def search_notes():
    question3 = input("Введите искомое слово: ")
    if (question3 == notes[0] or question == notes[1] or question == notes[2]  or question == notes[3]  or
            question == notes[4]  or question == notes[5]):
        for i in notes:
            print(i)
    else:
        print("Заметок не было найдено")

def exit_program():
    print("Вы вышли из программы")

notes = ['Алексей', 'Список покупок', 'Купить продукты на неделю', 'Новая',
         '27-11-2024', '30-11-2024']
menu = ["Создать новую заметку", "Показать все заметки", "Обновить заметку", "Удалить заметку",
        "Найти заметку", "Выйти из программы"]
for i in menu:
    print(i)
question = input("Введите нужную функцию: ")
if question == "Создать новую заметку":
    create_note()
elif question == "Показать все заметки":
    display_notes()
elif question == "Обновить заметку":
    update_note()
elif question == "Удалить заметку":
    delete_note()
elif question == "Найти заметку":
    search_notes()
elif question == "Выйти из программы":
    exit_program()

