try:
    number1 = int(input('Введите число: '))
    number2 = int(input('Введите Второе число: '))


    znak = input('Что-будем делать [+],[-],[*],[/] : ')

    plus = '+'
    minus = '-'
    m = '*'
    delit = '/'

    if znak == plus:
        print(number1 + number2)
    if znak == minus:
        print(number1 - number2)
    if znak == m:
        print(number1 * number2)
    if znak == delit:
        print(number1 / number2)
except Exception:
    print('Вы не верно ввели')


# year = 2023
# old = int(input('Введите свой возраст : '))
# text = 'Вы родились в'

# if old > 0:
#     print(text)
#     print(year - old)

# def add_numbers(a,b):
#     return a+b
# result = add_numbers(2,3)
# print(result)


# try:
#     x = int(input("number : "))
#     y = 10/x
#     print(y)
# except Exception:
#     print('Error')
# except ValueError:
#     print('Erorr number')




