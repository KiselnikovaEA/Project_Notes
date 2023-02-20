import model
import view

def button_click():
    view.hello_message()
    model.show_notes()  
    while True:
                # Показать заметки
        ids = model.get_ids()
        chosen_mode = view.choose_mode()    # Выбор действия
        if chosen_mode == '1':              # Создать заметку
            entry = view.entry_inp()
            model.create_note(entry, ids)
            view.note_created_message()
        elif chosen_mode == '2':            # Посмотреть заметку
            note_id = view.choose_note()
            if int(note_id) in ids:
                model.show_note(note_id)
            else:
                view.no_id_message()
        elif chosen_mode == '4':            # Удалить заметку
            note_id = view.choose_note()
            if int(note_id) in ids:
                model.delete_note(note_id)
                view.deleted_message()
            else:
                view.no_id_message()
        elif chosen_mode == '5':
            model.show_notes()
        elif chosen_mode == 'q':
            view.end_message()
            break
        else:
            view.error_message()
