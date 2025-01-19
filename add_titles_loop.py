question1_list = []
question2_list = []
question3_list = ""
question1 = input("Введите заголовок (или оставьте пустым для завершения): Основные идеи ")
while question1 != "":
    question1_list.append(question1)
    question1 = input("Введите заголовок (или оставьте пустым для завершения): Основные идеи ")
question2 = input("Введите заголовок (или оставьте пустым для завершения): Список задач ")
while question2 != "":
    question2_list.append(question2)
    question2 = input("Введите заголовок (или оставьте пустым для завершения): Список задач ")
question3 = input("Введите заголовок (или оставьте пустым для завершения): ")
if question3 != "":
    question3_list = question3
print("Заголовок заметки:", question3_list)
print("-Основные идеи:", question1_list)
print("-Список задач:", question2_list)
