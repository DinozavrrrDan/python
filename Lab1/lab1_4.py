users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
site_visitors = {"Общее количество": 0, "Уникальные посещения": 0}
site_visitors["Уникальные посещения"] = len(set(users))
site_visitors["Общее количество"] = len(users)
print(site_visitors)
