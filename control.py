# создаем словари для каждого юзера 
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': ' q2'}
account3 = {'login': 'olga', 'password': ' q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# создаем словари для каждого юзера
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account':  account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account' : account4}

# создаем список словарей для юзера
user_list = [user1, user2, user3, user4,]

# Вводим значение ключа и передаем значение ключа на user_key
# методом lower() приводим к нижнему регистру
user_key = input('введите ключ (name или account): ').lower()
print(user_key)
# в попытке выводим значение по ключю для каждого юзера
try:
    print(f'значение ключа {user_key} name для юзера = {user1[user_key]}')
    print(f'значение ключа {user_key} name для юзера = {user2[user_key]}')
    print(f'значение ключа {user_key} name для юзера = {user3[user_key]}')
    print(f'значение ключа {user_key} name для юзера = {user4[user_key]}')

except KeyError:
    # Если ключь в словаре не найден,то выводим сообщения об ошибке
    print('Введенный ключ не найден')
 
# Вводим порядковый номер юзера и передаем введенное значение на переменную user_number
user_number = input('Введите порядковый номер: ')

# С помощью функции int приводим введенное значение к целому числу   
user = user_list[int(user_number)-1]

# в попытке выводим все ключи словаря
try:
    print(f"данные по юзеру № {user_number}")
    print(f"имя: {user['name']}")
    print(f"возраст: {user['age']}")
    print(f"логин: {user['account']['login']}")
    print(f"пароль: {user['account']['password']}")
    
 # Если ключь в словаре не найден то выводим сообщения об ошибке.
except KeyError:
    print('Пользователь с указанным номером не найден.')
    
 # Вводим порядковый номер пользователя,котого нужно переместить в конец
user_number=input('Введите номер пользователя котого нужно переместить в конец:  ')
print('cписок до изменения: ')
print(user_list)

# С помощью функции pop() извлекаем элемент из списка user_list
# Функция pop() удалит элемент из списка и передаст его в переменную item_pop
item_pop = user_list.pop(int(user_number)-1)
print(f"Пользователь с именем {item_pop['name']} перемещен в конец")

# С помощью функции append() добавляем извлеченный элемент в список
#  Функция append() добавляет элемент в конец списка
user_list.append(item_pop)
print('Список после изменения:')
print(user_list)
