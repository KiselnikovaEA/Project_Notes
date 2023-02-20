import csv
import datetime
import os

def get_ids():
    with open('notes.csv', 'r', encoding='utf-8-sig') as notes:
        reader = csv.DictReader(notes, delimiter=';')
        ids = []
        for row in reader:
            ids.append(int(row["id"]))
        return ids

def show_notes():
    with open('notes.csv', 'r', encoding='utf-8-sig') as notes:
        reader = csv.DictReader(notes, delimiter=';')
        print("Ваши заметки:")
        for row in reader:
                print(f'{row["id"]}. {row["Дата"]}. {row["Заголовок"]}')

def create_note(entry, ids):
    now = datetime.datetime.now()
    entry.insert(0,now.strftime("%d-%m-%Y %H:%M"))
    if len(ids) > 0:
        entry.insert(0, max(ids) + 1)
    else:
        entry.insert(0, 0)
    attrs = ['id', 'Дата', 'Заголовок', 'Текст']
    dct = {attr: meaning for attr, meaning in zip(attrs, entry)}
    with open('notes.csv', 'a', encoding='utf-8-sig') as notes:
        writer = csv.DictWriter(notes, delimiter=';', fieldnames=attrs, lineterminator='\n')
        writer.writerow(dct)

def show_note(note_id):
    with open('notes.csv', 'r', encoding='utf-8-sig') as notes:
        reader = csv.DictReader(notes, delimiter=';')
        for row in reader:
                if row["id"] == str(note_id):
                    print(f'id: {row["id"]}\nДата: {row["Дата"]}\nЗаголовок: {row["Заголовок"]}\nТекст: {row["Текст"]}\n')

def delete_note(note_id):
    with open('notes.csv', 'r', encoding='utf-8-sig') as source:
        reader = csv.DictReader(source, delimiter=';')
        with open('notes_tmp.csv','a', encoding='utf-8-sig', newline='') as destination:
            writer = csv.DictWriter(destination, delimiter=';', fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(
            filter(lambda row: row.get('id') != note_id, reader)
            )
    os.remove('notes.csv')
    os.rename('notes_tmp.csv', 'notes.csv')