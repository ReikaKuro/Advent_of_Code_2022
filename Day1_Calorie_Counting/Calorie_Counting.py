'''
First half of day 1
'''
with open('elfs_resources.txt', 'r') as file:
    elf_resources = file.read()

elfs_calories_list = []

calories_sum = 0
elf_counter = 1
for elf_calories in elf_resources.split('\n'):
    try:
        calories_sum += int(elf_calories)
    except ValueError:
        elfs_calories_list.append([f'Elf No {elf_counter}', calories_sum])
        calories_sum = 0
        elf_counter += 1

most_calories = ['', 0]
for elf, calories in elfs_calories_list:
    if int(calories) > int(most_calories[1]):
        most_calories = [elf, calories]

print(f'{most_calories[0]} contains most calories: {most_calories[1]}')


'''
Second half of day 1
'''

top_three_elfs = [['', 0], ['', 0], ['', 0]]
for elf, calories in elfs_calories_list:
    for index, value in enumerate(top_three_elfs):
        if int(calories) > int(value[1]):
            top_three_elfs.insert(index, [elf, calories])
            top_three_elfs.pop(-1)
            break

top_three_calories = 0
for _, calories in top_three_elfs:
    top_three_calories += int(calories)

print(f'Top three elfs: {top_three_elfs}\nSum of Calories: {top_three_calories}')
