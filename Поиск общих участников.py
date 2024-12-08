def find_common_participants(participants_str1, participants_str2, separator=","):

    group1 = participants_str1.split(separator)
    group2 = participants_str2.split(separator)
    common_participants = sorted(list(set(group1) & set(group2)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники (с разделителем '|'): {common_participants}")

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники (с разделителем ','): {common_participants}")