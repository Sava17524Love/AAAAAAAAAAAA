import json

from PyQt5.QtWidgets import (QAppLication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout )

app = QAppLication([])

'''Інтерфейс програми'''

notes_win = QWidget()
notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)
list_notes = QListWidget()
list_notes_label = QLabel('Список заміток')
button_note_del = QPushButton('Створити замітку')
button_note_create = QPushButton('Видалити замітку')
button_note_save = QPushButton('заберигти замітку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('')
field_text = QTextEdit()
button_note_add = QPushButton('')
button_note_del = QPushButton('')
button_note_search = QPushButton('')
list_tags = QListWidget()
list_tags_label = QLabel()

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(list_notes)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_3.addWidget(button_note_add)
row_3.addWidget(button_note_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_note_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)
notes_win.show()

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Дотати замітку', 'Назва замітки' )
    if ok and note_name != '':
        notes[note_name] = {'текст': '', 'теги': []}
        list_notes.addItems(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)
button_note_create.clicked.connect(add_note())

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])
list_notes.itemClicked.connect(show_note)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key][''] = field_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('')
button_note_save.clicked(save_note)

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('замітка для видалення не вибрана!')
button_note_del.clicked.connect(del_note)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['']:
            notes[key][''].append(tag)
            list_tags.addItems(tag)
            field_tag.clear()
        with open('notes_date.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('')
button_note_add.clicked.connect(add_tag)

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_notes.selectedItems()[0].test()
        notes[key][''].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key][''])
        with open('notes_date.json', 'w') as file:
            json.dump(notes, sort_keys=True, ensure_ascii=False)
    else:
        print('')
button_note_del.clicked.connect(del_tag)

def search_tag():
    tag = field_tag.tag.text()
    if button_note_search.text() == '' and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['']:
                notes_filtered[note] = notes[note]

        button_note_search.setText('')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif button_note_search.text() == '':
        field_tag.clear()
        list_notes.clear()
        list_notes.addItems(notes)
        button_note_search.setText('')
    else:
        pass
button_note_search.clicked.connect(search_tag)

notes_win.show()

with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems((notes))

app.exec_()
