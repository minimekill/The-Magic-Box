import json


def distance(x1, x2):
    return x2 - x1


def to_jump_or_not_to_jump(x1, x2, enemy_height):
    out_distance = distance(x1, x2)

    data_upper = json.loads(open('jumpingParameter.json').read())
    data_lower = json.loads(open('jumpingParameter2.json').read())
    enemy_height = str(enemy_height)
    if enemy_height in data_upper and enemy_height in data_lower:
        number_upper = int(data_upper[enemy_height])
        number_lower = int(data_lower[enemy_height])

        number_accumulated = number_upper - (number_upper - number_lower) / 2

        if out_distance - 3 <= number_accumulated <= out_distance + 3:
            return True

    return False


'''def change_parameter(enemy_height):
    data = json.loads(open('jumpingParameter.json').read())
    if str(enemy_height) in data:
        data[str(enemy_height)] = int(data[str(enemy_height)]) - 1
    else:
        data[str(enemy_height)] = 100
    
    with open('jumpingParameter.json', 'w') as outfile:
        json.dump(data, outfile)'''