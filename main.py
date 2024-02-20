import json
import os
from datetime import datetime


def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes,file)

def read_notes():
    for note in notes:
        print(f"ID: {note['id']}Заголовок: {note['title']}Текст: {note['body']} Дата/Время: {note['timestamp']}")


def create_note():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note_id = len(notes) +1
    note_title = input("Введите заголовок записи: ")
    note_body = input("Введите текст записи: ")

    note = {
        "id": note_id,
        "title": note_title,
        "body": note_body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes()
    print("Запись создана")



def edit_notes():
    note_id = int(input("Введите ID заметки для редактирования: "))
    note_index = -1

    for index, note in enumerate(notes):
        if note['id'] == note_id:
            note_index = index
            break

    if note_index != -1:
        note_title = input("Введите новый заголовок записи: ")
        note_body = input("Введите новый текст записи: ")

        notes[note_index]['title'] = note_title
        notes[note_index]['body'] = note_body
        notes[note_index]['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        save_notes()


def delete_note(note_index=None):
    note_id = int(input("Введите ID записи для ее удаления: "))
    note_index -1
    for index, note in enumerate(notes):
        if note['id'] == note_id:
            note_index = index
            break

    if note_index != -1:
        del notes[note_index]
        save_notes()
        print("Запись удалена")
    else:
        print("Записи с таким ID не существует")



def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes.extend(json.load(file))


notes = []
load_notes()

while True:
    print("Меню: ")
    print("1. Создать запись")
    print("2. Посмотреть все записи")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_notes()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break

    else:
        print("Неверный выбор")

