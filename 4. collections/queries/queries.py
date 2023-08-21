queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

queries_count = {}

for query in queries:
    words = query.split()
    if len(words) in queries_count.keys():
        queries_count[len(words)] += 1
    else:
        queries_count.update({len(words): 1})

for key, value in queries_count.items():
    percent = round(value / len(queries) * 100, 2)
    print(f'Поисковых запросов из {key} слов: {percent}% ({value} запросов)')
