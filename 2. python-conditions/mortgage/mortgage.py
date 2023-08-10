mortgage_final = 2
region = input('Введите свой регион: ')

if region == 'Дальний Восток':
    mortgage_final = 2
else:
    child_amount = int(input('Сколько у вас детей? Напишите числом: '))
    salary_project = input('Есть ли у вас зарплатный проект? Напишите, да или нет ')
    insurance = input('Страхование будет оформлено в этом же банке? Напишите, да или нет ')

    if child_amount > 3:
        mortgage_final -= 1
    if salary_project.lower() == 'да':
        mortgage_final -= 0.5
    if insurance.lower() == 'да':
        mortgage_final -= 1.5

print(f'Ипотечная ставка составляет: {mortgage_final}%')
