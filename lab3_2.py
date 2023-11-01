# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, delimiter=','):
    set1 = set(str1.split(delimiter))
    set2 = set(str2.split(delimiter))
    final_list = list(set1.intersection(set2))
    final_list.sort()
    return final_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
