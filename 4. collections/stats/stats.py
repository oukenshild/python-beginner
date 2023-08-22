stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max(stats, key=stats.get)
max_channel = ''

for channel in stats.keys():
    if stats[channel] > stats.get(max_channel, 0):
        max_channel = channel

print(max_channel)
