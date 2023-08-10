symbol = str(input('Введите символ: '))

length_square = int(input('Введите длину стороны квадрата числом: '))
perimeter_square = length_square * 4

print('Периметр квадрата:', perimeter_square)
print('Площадь квадрата:', length_square * 2)

length_rectangle = int(input('Введите длину прямоугольника числом: '))
width_rectangle = int(input('Введите ширину прямоугольника числом: '))
surface_rectangle = length_rectangle * width_rectangle

print('Периметр прямоугольника:', length_rectangle * 2 + width_rectangle * 2)
print('Площадь прямоугольника:', surface_rectangle)

length_stroke = perimeter_square + surface_rectangle
print(length_stroke * symbol)

payment = int(input('Введите заработную плату в месяц числом: '))
percent_deposit = int(input('Введите, какой процент (%) уходит на ипотеку, числом: '))
percent_life = int(input('Введите, какой процент (%) уходит на жизнь, числом: '))
deposit = int(payment * percent_deposit / 100 * 12)
life = int(payment * percent_life / 100 * 12 - deposit)

print('На ипотеку было потрачено:', deposit, 'рублей')
print('Было накоплено:', life, 'рублей')