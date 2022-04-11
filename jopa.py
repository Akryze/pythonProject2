users_dict = dict()


def users_get():
    print('Текущая база данных:')
    for keys in users_dict:
        print('Nickname: ' + keys + ' | Passwrod: ' + users_dict[keys])


username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
users_dict[username] = password

print('Пользователь ' + username + ' успешно создан!')

users_get()

add_check = input('Хотите добавить ещё одного? y/n: ')

while add_check == 'y':
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    users_dict[username] = password
    print('Пользователь ' + username + ' успешно создан!')
    users_get()
    add_check = input('Хотите добавить ещё одного? y/n: ')
else:
    users_get()

