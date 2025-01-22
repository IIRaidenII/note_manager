all_notes = []
question_ = input("Добро пожаловать в 'Менеджер заметок'! Хотите добавить заметку? ")
while question_ == "Да":
    name = input("Введите имя: ")
    title = input("Введите заголовок: ")
    content = input("Введите описание: ")
    status = input("Введите статус (Новая, в процессе, выполнено): ")
    created_date= input("Дата создания (День.месяц.год): ")
    issue_date = input("Дата дедлайна (День.месяц.год): ")
    note1 = [name, title, content, status, created_date, issue_date]
    all_notes.append(note1)
    question_ = input("Хотите добавить ещё заметки ?")
if question_ == "Нет":
    print("Ваши заметки:")
    print(all_notes)
