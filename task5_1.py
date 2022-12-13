# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_abv = 'абвгде вбару негбв, абтур пабви'

def new_text(text_abv):
    text_abv = list(filter(lambda x: 'абв' not in x, text_abv.split()))
    return " ".join(text_abv)

text_abv = new_text(text_abv)
print(text_abv)