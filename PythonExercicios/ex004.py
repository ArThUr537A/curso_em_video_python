a = input('\033[4;32mDigite algo:\033[m ')
print('\033[30mO tipo primitivo desse valor é ', type(a))
print('\033[31mSó tem espaços?', a.isspace())
print('\033[32mÉ um número?', a.isnumeric())
print('\033[33mÉ alfabetico?', a.isalpha())
print('\033[34mÉ alfanumerico?', a.isalnum())
print('\033[35mEsta em maiusculas?', a.isupper())
print('\033[36mEsta em minusculas?', a.islower())
print('\033[37mEsta capitalizada?', a.istitle())