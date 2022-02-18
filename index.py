# инициализация перемонной                  while будет работать пока не будет FALSE
# while условие зависящая от перменной:
#     тело цикла

 # *   в цикле while условкие когда то должно стать FALSE
 # !   в условии есть переменная, которая должна меняться при каждом проходе цикла
 # !   переменная меняется в теле цикла
 # !   обычно перемнная являетс счетчиком


 # пример вывода чисел от 10 до 20 включательно:
 
# i = 10
# while i <= 20:
#     print (i)
#     i += 1

# i = -20
# while i <= 20:
#     print (i, end = '_')   # выполняй тело цикла, пока i меньше либа равно 20
#     i += 1

# for i in range(10,21):
#     print(i, end = '_')


# Пример вывода чисел от 200 до 150 включительно, десятками

# for i in range(200, 149, -10):
#     print(i, end = '_')

# i = 200
# while i >= 150:
#     print(i, end = '_')
#     i -= 10

# i = 150
# while i <= 200:
#     print(i, end = '_')
#     i += 10

# i = 200
# while i >= 150:
#     print(i, end = '_')
#     i -= 10





# name = 'Elbek'      #со строками должны внести индекс 

# i = 0
# while i < 5:
#     print(name[i], end = '_')
#     i += 1
    

# name = 'Hello, He is Elbek. How are you doing?'      #со строками должны внести индекс 

# i = 0
# while i < len(name):
#     print(name[i], end = '_')
#     i += 1

# name = 'Hello, He is Elbek. How are you doing?'

# for ltr in name:
#     print(ltr, end = '/')

# name = 'Hello, He is Elbek. How are you doing?'

# for i in range (len(name)):
#     print(name[i], end = '_')


# способы создать бесконечный цикл
# 1. Написать условие, которое всегда будет верным
# while 1 > 0:
#     pass


# 2. В условии написать TRUE
# while True:
#     pass


# Как остановить цикл который который бесконечный -> Нужно, чтобы консоль была активной и нажать -> Ctrl + C
# Как управлять циклом который бесконечный?
# Ответ -> м помощью if и break

# i = 0
# while True:
#     print('Elbek')
#     i += 1
#     if i == 10:
#         break


# 
# #

# while True:
#     num = int(input('Enter positive number: '))
#     if num < 0:
#         break


# int
# float
# bool True - False

# индексируемые объекты
# str
# list    - 
# списки -> []

# гомогенный список -> потому что в нём только СТРОКИ 
students = ['Umar', 'Abduvali', 'Oybek', 'Iskandar']
ages = [16, 16, 16, 13, 14, 15]
countries = ['Uzbekistan', 'Kazakhstan', 'USA', 'Poland', 'Sweden']
countries_codes = ['UZ', 'PO', 'UK', 'UA']


mobile_phones = ['Iphone', 'Samsung', 'Redmi', 'Xciaomi']
laptop_brands = ['Asus', 'Acer', 'Hp', 'Honor', 'Toshiba']
social_apps = ['TikTok', 'Instagram', 'Facebook', 'Twitter']
messangers = ['Whatsapp', 'Telegram']
games = ['Csgo', 'Dota2', 'Dota1', 'Gta']
planets = ['Venera', 'Earth', 'Jupiter']
types_of_clothes = ['jeans', 't-shirt', 'sneakers']
programs = ['Atom', 'Vscode', 'Sublime']
program_languages = ['Python', 'Java', 'Javascript', 'Html']
nationalityes = ['Uzbek', 'Kazakh', 'Chineese']
