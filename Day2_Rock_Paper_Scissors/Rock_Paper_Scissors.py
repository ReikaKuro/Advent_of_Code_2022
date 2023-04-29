'''
First half of day 2
'''

with open('input.txt', 'r') as file:
    scenario = file.read()

# [real_sign, sign_score, lose_to, win_to]
results_dict = {
    'X': ['A', 'B', 'C'],
    'Y': ['B', 'C', 'A'],
    'Z': ['C', 'A', 'B']
}

sign_points = {
    'A': 1,
    'B': 2,
    'C': 3
}

final_score = 0

for match in scenario.split('\n'):
    opponent_move = match[0]
    my_move = match[2]
    rounds_score = 0
    if opponent_move == results_dict[my_move][2]:
        my_sign = results_dict[my_move][0]
        rounds_score = 6 + sign_points[my_sign]
        print(f'{opponent_move} : {my_sign}, You got {rounds_score} Points')

    if opponent_move == results_dict[my_move][1]:
        my_sign = results_dict[my_move][0]
        rounds_score = 0 + sign_points[my_sign]
        print(f'{opponent_move} : {my_sign}, You got {rounds_score} Points')

    if opponent_move == results_dict[my_move][0]:
        my_sign = results_dict[my_move][0]
        rounds_score = 3 + sign_points[my_sign]
        print(f'{opponent_move} : {my_sign}, You got {rounds_score} Points')

    final_score += rounds_score

print(f'Your final score: {final_score}')
print(f'\n###################################\n')

'''
Second half of day 2
'''

# [win, draw, lose]
scenario_dict = {
    'A': ['B', 'A', 'C'],
    'B': ['C', 'B', 'A'],
    'C': ['A', 'C', 'B']
}

final_score = 0

for match in scenario.split('\n'):
    opponent_move = match[0]
    my_move = match[2]
    rounds_score = 0
    if my_move == 'X':
        my_sign = scenario_dict[opponent_move][2]
        rounds_score = 0 + sign_points[my_sign]
        print(f'{opponent_move} : {my_sign}, You got {rounds_score} Points')

    if my_move == 'Y':
        my_sign = scenario_dict[opponent_move][1]
        rounds_score = 3 + sign_points[my_sign]
        print(f'{opponent_move} : {my_sign}, You got {rounds_score} Points')

    if my_move == 'Z':
        my_sign = scenario_dict[opponent_move][0]
        rounds_score = 6 + sign_points[my_sign]
        print(f'{opponent_move} : {my_sign}, You got {rounds_score} Points')

    final_score += rounds_score

print(f'Your final score: {final_score}')
