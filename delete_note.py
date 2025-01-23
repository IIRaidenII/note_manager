all_notes = []
note1 = {"name1": "Мария", "title1": "Учеба", "content1": "Подготовиться к экзамену"}
note2 = {"name2": "Алексей", "title2": "Список покупок", "content2": "Купить продукты на неделю"}
all_notes.append(note1)
all_notes.append(note2)
print("1.", "Имя:", note1["name1"])
print("Заголовок:", note1["title1"])
print("Описание:", note1["content1"])
print("2.", "Имя:", note2["name2"])
print("Заголовок:", note2["title2"])
print("Описание:", note2["content2"])
question = input("\nХотите удалить какую-нибудь заметки ? ")
if question == "Да":
    question1 = input("Введите какое-нибудь слово из заметки ")
    if question1 == note1["name1"]:
        all_notes.remove(note1)
        print("2.", "Имя:", note2["name2"])
        print("Заголовок:", note2["title2"])
        print("Описание", note2["content2"])
    elif question1 == note1["title1"]:
        all_notes.remove(note1)
        print("2.", "Имя:", note2["name2"])
        print("Заголовок:", note2["title2"])
        print("Описание", note2["content2"])
    elif question1 == note1["content1"]:
        all_notes.remove(note1)
        print("2.", "Имя:", note2["name2"])
        print("Заголовок:", note2["title2"])
        print("Описание", note2["content2"])
    elif question1 == note2["name2"]:
        print("1.", "Имя:", note1["name1"])
        print("Заголовок:", note1["title1"])
        print("Описание", note1["content1"])
    elif question1 == note2["title2"]:
        print("1.", "Имя:", note1["name1"])
        print("Заголовок:", note1["title1"])
        print("Описание", note1["content1"])
    elif question1 == note2["content2"]:
        print("1.", "Имя:", note1["name1"])
        print("Заголовок:", note1["title1"])
        print("Описание", note1["content1"])
else:
    print("Удаление заметок отменено")