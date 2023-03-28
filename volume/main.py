data = input('Напишите что-нибудь: ')

with open('data.txt', 'a', encoding='utf-8') as file:
    print(data, file=file)

with open('data.txt', 'r', encoding='utf-8') as file:
    print(file.read())
