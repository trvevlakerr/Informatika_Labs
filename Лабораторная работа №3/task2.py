def find_common_participants(group1, group2, delimiter=","):
    return sorted(set(group1.split(delimiter)) & set(group2.split(delimiter)))


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")

print(find_common_participants("Иванов;Петров;Сидоров", "Петров;Сидоров;Смирнов", ";"))