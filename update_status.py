all_statuses = ("Выполнено", "В процессе", "Отложено")
status = "В процессе"
print ("Текущий статус заметки:", status)
question = input("Вы действительно хотите сменить статус заметки ? ")
if question != "Да":
    if question != "Нет":
        print("Некоректный ввод, попробуйте снова")
if question == "Нет":
    print("Вы отказались от смены статуса")
if question == "Да":
    print("1.", all_statuses[0])
    print("2.", all_statuses[1])
    print("3.", all_statuses[2])
    user_answer = input("Введите цифру нового статуса: ")
    if user_answer == "1":
        print("Статус заметки успешно обновлён на:", all_statuses[0])
    if user_answer == "2":
        print("Статус заметки успешно обновлён на:", all_statuses[1])
    if user_answer == "3":
        print("Статус заметки успешно обновлён на:", all_statuses[2])
