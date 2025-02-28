class BulletsJournal:
    def __init__(self):
        self.notes = []
        self.bullets = {
            'task': '•',
            'event': '○',
            'note': '-',
            'important': '!',
            'completed': '✓'
        }

    def show_bullets(self) -> None:
        for k, v in self.bullets.items():
            print(f'{k} - {v}')

    def show_notes(self) -> None:
        if self.notes:
            print("\n".join([f'{self.bullets[i[0]]} - {i[1]}' for i in self.notes]))
        else:
            print('Заметок не найдено')

    def add_notes(self, type_bullet: str, text: str) -> None:
        if type_bullet in self.bullets.keys():
            self.notes.append([type_bullet, text])
            print(f'Заметка добавлена:\n{self.bullets[type_bullet]} - {text}')
        else:
            print(f'Нету такого типа Bulletов. Доступные типы:\n{"\n".join([f'{k} - {v}'for k, v in self.bullets.items()])}')

    def delete_last_notes(self) -> None:
        try:
            self.notes.pop(len(self.notes) - 1)
            print('Последняя запись удалена')
            print(self.notes)
        except:
            print('Нет доступных записей вообще')

    def delete_number_notes(self, number: int) -> None:
        try:
            self.notes.pop(number - 1)
            print(f'Запись под номером {number} удалена успешно')
        except:
            print('Нету такого номера записи')

    def insert_into_index(self, index: int, type_bullet: str, text: str) -> None:
        if index > len(self.notes) + 1:
            print('Столько нету заметок')
        else:
            self.notes.insert(index - 1, [type_bullet, text])
            print(f'Успешно добавлена заметка с индексом {index}')




if __name__ == '__main__':
    journal = BulletsJournal()
    print('\033[36mДобро пожаловать в BulletConsole. Выберите действие: ')
    menu_text = '''\033[35m
    0 - Закрыть программу
    1 - Посмотреть все типы Bulletов
    2 - Посмотреть все добавленные заметки
    3 - Добавить заметку
    4 - Удалить последнюю заметку
    5 - Удалить заметку под опр. номером
    6 - Добавить заметку по индексу
    '''
    print(menu_text)
    choice = input('\033[31m Ваш выбор: ')

    while choice != '0':
        if choice == '1':
            journal.show_bullets()
            print(menu_text)
            choice = input('\033[31m Ваш выбор: ')
        elif choice == '2':
            journal.show_notes()
            print(menu_text)
            choice = input('\033[31m Ваш выбор: ')
        elif choice == '3':
            journal.show_bullets()
            bullet = input('Введите тип bulletа: ')
            text = input('Введите текст заметки: ')
            journal.add_notes(bullet, text)
            print(menu_text)
            choice = input('\033[31m Ваш выбор: ')
        elif choice == '4':
            journal.delete_last_notes()
            print(menu_text)
            choice = input('\033[31m Ваш выбор: ')
        elif choice == '5':
            number = int(input('Введите номер заметки: '))
            journal.delete_number_notes()
            print(menu_text)
            choice = input('\033[31m Ваш выбор: ')
        elif choice == '6':
            index = int(input('Введите индекс заметки: '))
            bullet = input('Введите тип bulletа: ')
            text = input('Введите текст заметки: ')
            journal.insert_into_index(index, bullet, text)
            print(menu_text)
            choice = input('\033[31m Ваш выбор: ')
        else:
            print('\033[31mЯ не знаю такой команды. Пожалуйста, введите то, что есть')
            print(menu_text)
            choice = input('\033[31m Ваш выбор: ')

    print('\033[35mПока-пока =)')
