boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Greg']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha', 'Emmy']

if len(sorted(boys)) != len(sorted(girls)):
    print('Мы не сможем никого познакомить — кто-то может остаться без пары!')
else:
    print('Идеальные пары: ')
    for boy, girl in zip(sorted(boys), sorted(girls)):
        print(boy, 'и', girl)
