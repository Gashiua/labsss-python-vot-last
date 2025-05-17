import re

# Открываем файл text.txt для чтения
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()  

# Ищем email-адреса с помощью регулярного выражения
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text)

# Ищем номера телефонов в формате +7-XXX-XXX-XX-XX
phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)

# Ищем слова, начинающиеся с заглавной буквы 
capital_words = re.findall(r'\b[А-ЯЁ][а-яё]*\b', text)

# Записываем найденные email-адреса в файл emails.txt
with open('emails.txt', 'w', encoding='utf-8') as file:
    for email in emails:
        file.write(email + '\n') 

# Записываем номера телефонов в файл phones.txt
with open('phones.txt', 'w', encoding='utf-8') as file:
    for phone in phones:
        file.write(phone + '\n') 

# Записываем слова с заглавной буквы в файл capital_words.txt
with open('capital_words.txt', 'w', encoding='utf-8') as file:
    for word in capital_words:
        file.write(word + '\n') 