information = {
"Name":str(input("Введите своё имя: ")),
"Content":str(input("Введите содержание заметки: ")),
"Status":str(input("Введите статус заметки: ")),
"Created_date":str(input("Введите дату создания: ")),
"Issue_date":str(input("Введите дату истечения: "))
}
tips = {
"tip1":str(input("Введите первую заметку: ")),
"tip2":str(input("Введите вторую заметку: "))
}

print("Ваше имя:", information["Name"])
print("Содержание заметки:", information["Content"])
print("Статус:", information["Status"])
print("Дата создания:", information["Created_date"])
print("Дата изменения:", information["Issue_date"])
print("Первый заголовок:", tips["tip1"], "; Второй заголовок:", tips["tip2"])

