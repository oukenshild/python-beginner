payment = int(input('Введите заработную плату в месяц числом: '))
percent_deposit = int(input('Введите, какой процент (%) уходит на ипотеку, числом: '))
percent_life = int(input('Введите, какой процент (%) уходит на жизнь, числом: '))
deposit = int(payment * percent_deposit / 100 * 12)
life = int(payment * percent_life / 100 * 12 - deposit)

print('На ипотеку было потрачено:', deposit, 'рублей')
print('Было накоплено:', life, 'рублей')